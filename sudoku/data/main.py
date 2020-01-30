"""import sys


def isValidPos(a, row, col, val):
    for i in (1, 10, 1):
        if a[row][i] == val:
            return 0
    for j in (1, 10, 1):
        if a[j][col] == val:
            return 0

    r = row / 3
    c = col / 3
    for i in (3 * r, 3 * (r + 1), 1):
        for j in (3 * col, 3 * (col + 1)):
            if a[i][j] == val:
                return 0
    return 1


def solve(a):
    row = 0
    col = 0
    flag = 0
    for i in (1, 10, 1):
        for j in (1, 10, 1):
            if a[i][j] == 0:
                row = i
                col = j
                flag = 1
                break

    if flag == 0:
        return 1

    for i in (1, 10, 1):
        if isValidPos(a, row, col, i):
            a[row][col] = i
            if solve(a):
                return 0
            a[row][col] = 0
    return 0


def main():
    arr = sys.argv[1]
    flag = solve(arr)
    if flag == 0:
        arr[0][0] = -1
    for i in (1, 10, 1):
        for j in (1, 10, 1):
            print(arr[i][j])
    return arr
"""