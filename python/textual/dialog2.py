import os
import subprocess
from textual.app import App, View, Layout, Placeholder, Button, Label


class GitRepoList(View):
    """A list of git repositories in the current directory."""

    def __init__(self):
        self.repos = self.get_repos()
        self.list = []
        for repo in self.repos:
            status = self.get_status(repo)
            self.list.append(
                Label(f"{os.path.basename(repo)} {repo} {status}"))
        super().__init__(self.list)

    def get_repos(self):
        """Get a list of git repositories in the current directory."""
        repos = []
        for dirpath, dirnames, filenames in os.walk('.'):
            if '.git' in dirnames:
                repos.append(dirpath)
        return repos

    def get_status(self, repo):
        """Get the status of a git repository."""
        proc = subprocess.run(
            ['git', '-C', repo, 'status', '--short'], capture_output=True)
        if proc.stdout:
            return '✗'
        else:
            return '✓'


class MainScreen(View):
    """The main screen of the user interface."""

    def __init__(self):
        self.repo_list = GitRepoList()
        self.update_button = Button("Update", self.update_repo)
        self.quit_button = Button("Quit", self.quit)
        super().__init__(
            [self.repo_list, self.update_button, self.quit_button])

    def update_repo(self):
        """Update the currently selected repository."""
        repo = self.repo_list.repos[self.repo_list.get_focus()]
        subprocess.run(['git', '-C', repo, 'pull'])
        self.repo_list.reload()

    def quit(self):
        """Quit the user interface."""
        raise SystemExit


if __name__ == '__main__':
    app = App(MainScreen())
    app.run()
