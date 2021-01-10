#Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
#alphabetical order
#
#You can either enter the text from the keyboard or
#initialize a string variable with the string


entry = input("Please enter a text")
vowels={"a", "e" ,"i", "o","u"}

finalSet = set(entry).difference(vowels)
print(finalSet)

finalList = sorted(finalSet)
print(finalList)
