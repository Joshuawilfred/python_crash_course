#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        j = 0
        for k in range(len(i)):
            print("{:d}".format(i[k]), end="" if k < len(i) - 1 else "\n")
            j += 1
            if len(matrix[0]) == 0:
                print("{}".format("))
