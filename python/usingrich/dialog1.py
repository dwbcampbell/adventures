# Description: python script generated in response to prompt #1
# It uses the rich.prompt.Prompt class to ask the user to select an action
# but it does not display the list of actions

from rich.prompt import Prompt
from rich.text import Text

# Define a list of actions
actions = ["Option 1", "Option 2", "Option 3"]

# Create a prompt with the list of actions
prompt = Prompt(choices=actions)

# Ask the user to select an action
selected_action = prompt.ask("Please select an action:")

# Print the selected action
print(f"You selected: {selected_action}")
