#!/usr/bin/python3
"""This module defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """Generates Pascal's Triangle of size 'n'.

    Args:
        n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle with 'n' rows.

    Examples:
        >>> pascal_triangle(4)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    """
    if n <= 0:
        return []

    p_triangles = [[1]]
    while len(p_triangles) != n:
        tri_last = p_triangles[-1]
        tri_temp = [1]
        for i in range(len(tri_last) - 1):
            tri_temp.append(tri_last[i] + tri_last[i + 1])
        tri_temp.append(1)
        p_triangles.append(tri_temp)

    return p_triangles
