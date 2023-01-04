#!/usr/bin/python3
"""Define text_indentation"""
def text_indentation(text):
    """Core of class"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1
    while c < len(text):
        print(text[c], end="")
        if text[c] == '\n' or text[c] in ".?:":
            if text[c] in ".?:":
                print('\n')
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1

