name = input("What is your name ? ")
age = int(input ("How old are you?"))

if 18 <= age < 31:
    print("You can go to vacation {0}".format(name))
else:
    print("go away somewhere else")
