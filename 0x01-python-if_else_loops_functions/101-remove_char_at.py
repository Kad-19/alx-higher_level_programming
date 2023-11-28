#!/usr/bin/python3
def remove_char_at(str, n):
    text = ""
    j = 0
    for i in str:
        if j == n:
            j += 1
            continue
        else:
            text += i
        j += 1
    return text
