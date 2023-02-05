import os
import subprocess
from textual.app import App, ComposeResult
from textual.widgets import DataTable


class TableApp(App):
    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("Repository", "Path", "Branch", "Status")
        for dirpath, dirnames, filenames in os.walk('.'):
            if '.git' in dirnames:
                repo_path = dirpath
                repo_name = os.path.basename(dirpath)
                repo_branch = self.get_branch(repo_path)
                repo_status = self.get_status(repo_path)
                table.add_row(repo_name, repo_path, repo_branch, repo_status)

    def get_branch(self, repo_path):
        """Get the current branch of a git repository."""
        proc = subprocess.run(['git', '-C', repo_path, 'rev-parse',
                              '--abbrev-ref', 'HEAD'], capture_output=True, text=True)
        return proc.stdout.strip()

    def get_status(self, repo_path):
        """Get the status of a git repository."""
        proc = subprocess.run(
            ['git', '-C', repo_path, 'status', '--short'], capture_output=True)
        if proc.stdout:
            return '✗'
        else:
            return '✓'


if __name__ == "__main__":
    app = TableApp()
    app.run()
