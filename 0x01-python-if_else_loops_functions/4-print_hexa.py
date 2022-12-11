#!/usr/bin/python3
import string
num = 0
while num <= 98:
    to_hex = hex(num)
    print("{} = {}".format(num, to_hex))
    num = num + 1
