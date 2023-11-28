#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number % 10
if number < 0:
    n -= 10
if n > 5:
    str = "greater than 5"
elif n == 0:
    str = "0"
else:
    str = "less than 6 and not 0"
print(f"Last digit of {number} is {n} and is {str}")
