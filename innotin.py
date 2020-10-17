parrot = " Norwegian Blue"

letter = input("Enter a Character: ")

if letter in parrot:
    print("{} is in {}".format(letter,parrot))
else:
    print("Nope")