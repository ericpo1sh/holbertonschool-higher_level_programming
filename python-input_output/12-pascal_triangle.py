#!/usr/bin/python3
""" pascal_triangle Module """


def pascal_triangle(n):
    """ Initializing pascal triangle function """
    rows = []
    if n <= 0:
        return rows

    rows.append([1])

    for i in range(1, n):
        row = []
        for j in range(0, i+1):
            if j == 0 or j ==i:
                row.append(1)
            else:
                prev = rows[i - 1]
                row.append(prev[j - 1] + prev[j])
        rows.append(row)
    return rows
if __name__ == '__main__':
    result = pascal_triangle(n)
    print(result)
