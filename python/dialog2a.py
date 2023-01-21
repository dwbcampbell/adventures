# Description: Prompt example 2a - Prompt with a list of choices
# It prints a list of actions and then asks the user to select an action

from rich.prompt import Prompt
from rich.text import Text

# Define a list of actions
actions = ["Option 1", "Option 2", "Option 3"]

# Create a prompt with the list of actions
prompt = Prompt(choices=actions)

# Print the list of actions
print("Available actions:")
for action in actions:
    print(f"- {action}")

# Ask the user to select an action
selected_action = prompt.ask("Please select an action:")

# Print the selected action
print(f"You selected: {selected_action}")
