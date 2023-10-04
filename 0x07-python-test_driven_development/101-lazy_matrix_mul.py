#!/usr/bin/python3

"""
Matrix Multiplication Function
This module contains a function for multiplying two matrices using NumPy.

"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
    Usage:
    result_matrix = lazy_matrix_mul(matrix_a, matrix_b)

    Args:
        matrix_a (list of lists of ints/floats): The first matrix to
        be multiplied.
        matrix_b (list of lists of ints/floats): The second matrix to
        be multiplied.

    Returns:
        numpy.ndarray: A new matrix representing the result of the
        multiplication.
    """

    return (np.matmul(m_a, m_b))
