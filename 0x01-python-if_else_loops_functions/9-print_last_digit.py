#!/usr/bin/python3
def print_last_digit(number):
    r = number % 10
    if number < 0:
        r = 10 - r
    print("{}".format(r), end="")
    return r
