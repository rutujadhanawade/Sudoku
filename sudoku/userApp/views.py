from django.shortcuts import render
import os

a = [[4, 0, 9, 0, 0, 8, 0, 3, 0],
     [7, 5, 0, 0, 3, 2, 0, 1, 8],
     [0, 0, 0, 5, 0, 0, 2, 0, 6],
     [8, 0, 0, 0, 0, 3, 9, 0, 0],
     [0, 3, 0, 0, 4, 0, 0, 7, 5],
     [0, 0, 1, 2, 0, 7, 0, 0, 0],
     [0, 0, 8, 4, 0, 0, 0, 0, 9],
     [0, 1, 0, 0, 0, 9, 0, 4, 0],
     [2, 0, 0, 7, 1, 0, 8, 5, 0]];


def index(request):
    return render(request, 'userApp/page1.html', {'a': a})


def solve():
    global a
    a = os.popen('python data/main.py'.format(a))


def answer(request):
    solve()
    ans = 1
    # if a[0][0] == -1:
    #    ans = 1
    global a
    return render(request, 'userApp/page2.html', {'a': a, 'ans': ans, 'msg': 'No solution possible.. :('})
