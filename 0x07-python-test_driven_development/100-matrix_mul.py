#!/usr/bin/python3
"""

This module contains a function that multiplies 2 matrices

"""


def matrix_mul(m_a, m_b):
    """
    Matrix Multiplication Function

    This module contains a function for multiplying two matrices.

    Usage:
        result_matrix = matrix_mul(matrix_a, matrix_b)

    Args:
        matrix_a (list of lists of int/float): The first matrix to be
        multiplied.
        matrix_b (list of lists of int/float): The second matrix to be
        multiplied.

    Raises:
        TypeError: If either matrix_a or matrix_b is not a list.
        TypeError: If either matrix_a or matrix_b is not a list of lists.
        TypeError: If an element in the lists is not an int or float.
        TypeError: If the rows of matrix_a or matrix_b have different sizes.
        ValueError: If either matrix_a or matrix_b is empty.
        ValueError: If matrix_a and matrix_b cannot be multiplied.

    Returns:
        list of lists of int/float: A new matrix representing the result of
        the multiplication.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [number for row in m_a for number in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [number for row in m_b for number in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    first_matrix = []
    for i in range(len(m_b[0])):
        new_row = []
        for j in range(len(m_b)):
            new_row.append(m_b[j][i])
        first_matrix.append(new_row)

    matrix2 = []
    for row in m_a:
        new_row = []
        for column in first_matrix:
            product = 0
            for m in range(len(first_matrix[0])):
                product += row[m] * column[m]
            new_row.append(product)
        matrix2.append(new_row)

    return matrix2
