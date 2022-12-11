#!/usr/bin/python3
letter = 122
while letter > 96:
    if abs(letter % 2) == 0:
        print("{}".format(chr(letter)), end="")
    else:
        print("{}".format(chr(letter - 32)), end="")
    letter = letter - 1
