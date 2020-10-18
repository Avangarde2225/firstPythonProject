available_exits = ["north", "south", "east", "west"]

chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please enter a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break
print("Are you good here")
