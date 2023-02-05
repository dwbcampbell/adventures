import os
import subprocess
from textual.app import App, ComposeResult
from textual.widgets import DataTable


class TableApp(App):
    BINDINGS = [("q", "quit", "Quit the application"),
                ("r", "refresh", "Refresh the table")]

    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        self.table = self.query_one(DataTable)
        self.refresh()

    def refresh(self) -> None:
        """Refresh the table with current data."""
        self.table.clear()
        self.table.add_columns("Repository", "Path", "Branch", "Status")
        for dirpath, dirnames, filenames in os.walk('.'):
            if '.git' in dirnames:
                repo_path = dirpath
                repo_name = os.path.basename(dirpath)
                repo_branch = self.get_branch(repo_path)
                repo_status = self.get_status(repo_path)
                self.table.add_row(repo_name, repo_path,
                                   repo_branch, repo_status)

    def get_branch(self, repo_path):
        """Get the current branch of a git repository."""
        proc = subprocess.run(['git', '-C', repo_path, 'rev-parse',
                              '--abbrev-ref', 'HEAD'], capture_output=True, text=True)
        return proc.stdout.strip()

    def get_status(self, repo_path):
        """Get the current status of a git repository."""
        proc = subprocess.run(
            ['git', '-C', repo_path, 'status', '--porcelain'], capture_output=True, text=True)
        if proc.stdout:
            return "Not Up-to-date"
        else:
            return "Up-to-date"

    def action_quit(self):
        """Quit the application."""
        self.stop()

    def action_refresh(self):
        """Refresh the table data."""
        self.refresh()


if __name__ == "__main__":
    app = TableApp()
    app.run()
