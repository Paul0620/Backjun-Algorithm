# 10828 스택 실4

from collections import deque
from sys import stdin

n = int(input())
que = deque([])
n_list = []


for _ in range(n):
    order = stdin.readline().split()
    n_list.append(order)

for i in n_list:
    if i[0] == "push":
        x = int(i[1])
        que.append(x)
    elif i[0] == "pop":
        if len(que) > 0:
            temp = que.pop()
        else:
            temp = -1
        print(temp)
    elif i[0] == "size":
        temp = len(que)
        print(temp)
    elif i[0] == "empty":
        if len(que) == 0:
            temp = 1
        else:
            temp = 0
        print(temp)
    elif i[0] == "top":
        if len(que) > 0:
            temp = que[-1]
        else:
            temp = -1
        print(temp)

