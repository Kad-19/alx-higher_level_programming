#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxim = 0
    for x, y in a_dictionary.items():
        if y > maxim:
            maxim = y
            key = x
    return key
