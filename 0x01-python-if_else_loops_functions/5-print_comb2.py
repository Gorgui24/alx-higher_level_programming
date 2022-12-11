#!/usr/bin/python3
import string
num = 0
while num <= 99:
    if num == 99:
        print(num)
    else:
        print("{:02}".format(num), end = ", " )
    num = num + 1
