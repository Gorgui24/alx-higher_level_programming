#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = 0
if number < 0:
    number = 0 - number
    last_digit = number % 10
    number  = 0 - number
    last_digit = 0 - last_digit
else:
    last_digit = number % 10
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
if last_digit <= 5 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
if last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
