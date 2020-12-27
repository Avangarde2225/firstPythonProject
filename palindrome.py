def is_palindrome(string):
    return string[::-1] == string
    # backwards = string[::-1]
    # return backwards == string


def  palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string +=char


    return string[::-1].casefold() == string.casefold()



word = input("Please enter a word to reverse: ")
if palindrome_sentence(word):
#if is_palindrome(word.casefold()):
    print("{} is a palindrome".format(word))
else:
    print("{} is not a palindrome".format(word))



