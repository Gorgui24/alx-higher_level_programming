#!/usr/bin/python3
import string
for letter in string.ascii_lowercase:
    if letter != 'e' and letter != 'q':
        print(letter, end="")
