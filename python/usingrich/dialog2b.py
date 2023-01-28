# Description: Present a list of actions using rich.table.Table
# and then ask the user to select an action
#
# As generated,
# 1. it did not include the necessary import statements
# 2. It did not define a prompt object
# 3. It used a raw print statement to display the table instead of
# using the Console object
#
# The following includes the necessary corrections

from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console

# Define a list of actions
actions = [["Option 1"], ["Option 2"], ["Option 3"]]

# Create a prompt with the list of actions
prompt = Prompt(choices=actions)

# Create table
table = Table(title="Available actions")
table.add_column("Actions")

for action in actions:
    table.add_row(*action)

console = Console()
console.print(table)

# Ask the user to select an action
selected_action = prompt.ask("Please select an action:")

# Print the selected action
console.print(f"You selected: {selected_action}")
