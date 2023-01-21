from rich.table import Table

# Define a list of actions
actions = [["Option 1"], ["Option 2"], ["Option 3"]]

# Create table
table = Table(title="Available actions")
table.add_column("Actions")

for action in actions:
    table.add_row(*action)

print(table)

# Ask the user to select an action
selected_action = prompt.ask("Please select an action:")

# Print the selected action
print(f"You selected: {selected_action}")
