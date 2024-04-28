#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """
        returns a list of lists of integers
        representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    pas_t = [[1]]
    for row_no in range(1, n):
        row = [1]
        for j in range(1, row_no):
            el = pas_t[row_no - 1][j - 1] + pas_t[row_no - 1][j]
            row.append(el)
        row.append(1)
        pas_t.append(row)

    return pas_t
