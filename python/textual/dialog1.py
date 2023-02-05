import os
import subprocess
import urwid


class GitRepoList(urwid.WidgetWrap):
    """A list of git repositories in the current directory."""

    def __init__(self):
        self.repos = self.get_repos()
        self.listbox = urwid.ListBox(
            urwid.SimpleFocusListWalker(self.get_list()))
        super().__init__(self.listbox)

    def get_repos(self):
        """Get a list of git repositories in the current directory."""
        repos = []
        for dirpath, dirnames, filenames in os.walk('.'):
            if '.git' in dirnames:
                repos.append(dirpath)
        return repos

    def get_list(self):
        """Get a list of widgets for the git repositories."""
        widgets = []
        for repo in self.repos:
            status = self.get_status(repo)
            widgets.append(urwid.Columns([
                ('fixed', 15, urwid.Text(os.path.basename(repo))),
                ('fixed', 15, urwid.Text(repo)),
                urwid.Text(status)
            ]))
        return widgets

    def get_status(self, repo):
        """Get the status of a git repository."""
        proc = subprocess.run(
            ['git', '-C', repo, 'status', '--short'], capture_output=True)
        if proc.stdout:
            return '✗'
        else:
            return '✓'


class MainScreen(urwid.WidgetWrap):
    """The main screen of the user interface."""

    def __init__(self):
        self.repo_list = GitRepoList()
        self.update_button = urwid.Button('Update')
        self.quit_button = urwid.Button('Quit')
        self.update_button.on_press = self.update_repo
        self.quit_button.on_press = self.quit
        self.pile = urwid.Pile([
            self.repo_list,
            urwid.Columns([
                ('fixed', 10, self.update_button),
                ('fixed', 10, self.quit_button)
            ])
        ])
        super().__init__(urwid.Filler(self.pile))

    def update_repo(self, button):
        """Update the currently selected repository."""
        focus_widget, _ = self.repo_list.listbox.get_focus()
        repo = self.repo_list.repos[self.repo_list.listbox.focus_position]
        subprocess.run(['git', '-C', repo, 'pull'])
        self.repo_list.reload()

    def quit(self, button):
        """Quit the user interface."""
        raise urwid.ExitMainLoop()


if __name__ == '__main__':
    main_screen = MainScreen()
    urwid.MainLoop(main_screen).run()
