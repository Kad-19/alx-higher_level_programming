#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
        return
    for lis in matrix:
        for i in lis:
            print("{:d}".format(i), end=" " if i != lis[-1] else '\n')
