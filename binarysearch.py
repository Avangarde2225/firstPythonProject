low = 1
high = 1000

print("Please guess a number between {} and {}".format(low,high))
input("Press ENTER to start")

guess = 1
while True:
    print("\tGuessing in the range of {} and {}".format(low,high))
    guesses = low + (high - low) // 2
    high_low = input("My guess is that {}. Should I guess higher or lower?" 
                     "Enter h or l or c if my guess is correct "
                     .format(guesses).casefold())

    if high_low == "h":
        #pass
        low = guesses + 1
    elif high_low == "l":
        #pass
        high = guesses - 1
    elif high_low == "c":

        print("I got it in {} guesses".format(guess))
        break
    else:
        print("Please enter  h, l or c!")

    guess = guess + 1





