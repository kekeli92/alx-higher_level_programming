#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            result += chr(ord(char) - ord('a') + ord('A'))
        else:
            result += char
    print("{}".format(result), end='\n')
