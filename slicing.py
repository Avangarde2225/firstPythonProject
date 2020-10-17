number = "9,222,323,424,222,098,288"
print(number[1::4]) #extracts the every 4th character in the function

Number = "9,222;323:424 222,098;288"
separators = Number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

letters = "abcdefghijklmnopqrstuvxyz"
print(letters[25:0:-1])     #backwards not including "a"

print(letters[25::-1]) # printing backwards inclugding a

print(letters[::-1]) #also works including a

# produce letters qpo

print(letters[16:13:-1])

#edcba
print(letters[4::-1])

#last 8 characters
print(letters[:-9:-1])

