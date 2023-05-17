#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    var = []
    for i in range(len(matrix)):
        var.append(list(map(lambda x: x ** 2, matrix[i])))

    return var
