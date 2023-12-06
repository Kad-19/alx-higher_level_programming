#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete = []
    for i in a_dictionary:
        if value == a_dictionary[i]:
            delete.append(i)
    for x in delete:
        if x in a_dictionary:
            del a_dictionary[x]
    return a_dictionary
