#!/usr/bin/python3
def uppercase(str):
    for i in str:
        j = ord(i)
        if ord(i) > 96 and ord(i) < 123:
            j -= 32
        print("{}".format(chr(j)), end="")
    print("")
