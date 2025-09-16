# https://www.codewars.com/kata/52223df9e8f98c7aa7000062/train/python

def rot13(message):
    abc = "abcdefghijklmnopqrstuvwxyz"
    
    message =  list(message)
    
    output = ""
    
    for char in message:
        if char.isalpha():
            if char.isupper():
                cp = (ord(char) - 52) % 26
                output += abc[cp].upper()
            else:
                cp = (ord(char) - 84) % 26
                output += abc[cp]
        else:
            output += char
    return output
