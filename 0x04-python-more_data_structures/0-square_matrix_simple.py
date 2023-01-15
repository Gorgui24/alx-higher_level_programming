#!/usr/bin/python3
""" square_matrix_simple - define class to print matrix"""
def square_matrix_simple(matrix=[]):
    return [list(map(lambda n: n**2, m)) for m in matrix]
