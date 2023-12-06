#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    result = 0
    count = 0
    for i in my_list:
        result += (i[0] * i[1])
        count += i[1]
    return result / count
