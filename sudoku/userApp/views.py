from django.shortcuts import render

"""
a = ([[4, 0, 9, 0, 0, 8, 0, 3, 0],
      [7, 5, 0, 0, 3, 2, 0, 1, 8],
      [0, 0, 0, 5, 0, 0, 2, 0, 6],
      [8, 0, 0, 0, 0, 3, 9, 0, 0],
      [0, 3, 0, 0, 4, 0, 0, 7, 5],
      [0, 0, 1, 2, 0, 7, 0, 0, 0],
      [0, 0, 8, 4, 0, 0, 0, 0, 9],
      [0, 1, 0, 0, 0, 9, 0, 4, 0],
      [2, 0, 0, 7, 1, 0, 8, 5, 0]])
"""
a = ([[0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0]])


def index(request):
    return render(request, 'userApp/intro.html')


def solve(request):
    return render(request, 'userApp/solve.html')


def make_que(request):
    return render(request, 'userApp/question.html', {'a': a})


def find_ans(request):
    global a
    ans_arr = main(a)
    ans = 1
    # if a[0][0] == -1:
    #    ans = 1
    return render(request, 'userApp/answer.html', {'ans_arr': ans_arr, 'ans': ans, 'msg': 'No solution possible.. :('})


def isValidPos(arr, row, col, val):
    for i in (0, 8, 1):
        if arr[row][i] == val:
            return 0
    for j in (0, 8, 1):
        if arr[j][col] == val:
            return 0

    r = int(row / 3)
    c = int(col / 3)
    for i in (3 * r, 3 * (r + 1) - 1, 1):
        for j in (3 * c, 3 * (c + 1) - 1, 1):
            if arr[i][j] == val and j != 9 and i != 9:
                return 0
    return 1


def solve(arr):
    row = 0
    col = 0
    flag = 1
    for i in a:
        for j in i:
            if j == 0:
                row = i
                col = j
                flag = 0
                break

    if flag == 0:
        return 1

    for i in (0, 8, 1):
        if isValidPos(arr, row, col, i):
            arr[row][col] = i
            if solve(arr):
                return 0
            arr[row][col] = 0
    return 0


def main(arr):
    flag = solve(arr)
    if flag == 0:
        arr[0][0] = -1
    for i in arr:
        for j in i:
            print(j)
    return arr
