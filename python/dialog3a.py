from rich.prompt import Prompt
from rich.table import Table

# Define a list of actions
actions = [["Option 1"], ["Option 2"], ["Option 3"], ["Quit"]]

# Create table
table = Table(title="Available actions")
table.add_column("Actions")

for action in actions:
    table.add_row(*action)

# Ask the user to select an action
while True:
    print(table)
    selected_action = prompt.ask("Please select an action:")
    if selected_action == "Quit":
        break
    else:
        print(f"You selected: {selected_action}")
