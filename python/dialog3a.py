# Description: The same as previous snippet but it uses a while loop

# As generated,
# 1. it did not define a prompt object
# 2. It used a raw print statement to display the table instead of
# using the Console object

from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console

# Define a list of actions
actions = [["Option 1"], ["Option 2"], ["Option 3"], ["Quit"]]

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
while True:
    console.print(table)
    selected_action = prompt.ask("Please select an action:")
    if selected_action == "Quit":
        break
    else:
        console.print(f"You selected: {selected_action}")
