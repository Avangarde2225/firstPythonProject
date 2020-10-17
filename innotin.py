parrot = " Norwegian Blue"

letter = input("Enter a Character: ")

if letter in parrot.casefold():  # not in can be added here as well
    print("{} is in {}".format(letter,parrot))
else:
    print("Nope")

