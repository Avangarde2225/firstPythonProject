name = input("Please enter your name")
age = int(input("How old are you {0} ?".format(name)))
print(age)

if age >= 18:
    print("You are eligible for voting")
else:
    print("come back in {0} years".format(18-age))

