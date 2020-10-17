number = "9,222,323,424,222,098,288"
print(number[1::4]) #extracts the every 4th character in the function

Number = "9,222;323:424 222,098;288"
separators = Number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])