# Description: This is just a copy of the previous snippet but it asks for confirmation

while True:
    print(table)
    selected_action = prompt.ask("Please select an action:")
    if selected_action == "Quit":
        confirm = prompt.confirm("Are you sure you want to quit?")
        if confirm:
            break
        else:
            continue
    else:
        print(f"You selected: {selected_action}")
