answer = 5

print("Please guess a number between 1 and 10")
guess = int(input())

if guess == answer:
    print("You got it!")
else:
    if guess < answer:
        print("Please guess a higher number")
    else:
        print("Please guess a lower number")
    guess = int(input())
    if guess == answer:
            print("You got it!")
    else:
            print("Next time dude!")








# if guess < answer:
#     print("Please guess higher")
#     guess=int(input())
#     if guess == answer:
#         print("Well done!")
#     else:
#         print("Nope")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done!")
#     else:
#         print("Nope")
# else:
#     print("You got it at the first time")


