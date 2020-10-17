age = 24
print("My age is " + str(age) + " years old.")

print("My age is {0} years old.".format(24))

for i in range(1,13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

for i in range(1,13): #left and center(^) aligned
    print("No. {0:<2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))
