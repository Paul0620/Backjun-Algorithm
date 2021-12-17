# 10866 덱 실4

from collections import deque
from sys import stdin

n = int(input())
order_list = []
que = deque()

for _ in range(n):
    order = stdin.readline().split()
    order_list.append(order)

for i in order_list:
    if i[0] == "push_front":
        x = int(i[1])
        que.appendleft(x)
    elif i[0] == "push_back":
        x = int(i[1])
        que.append(x)
    elif i[0] == "pop_front":
        if len(que) > 0:
            temp = que.popleft()
        else:
            temp = -1
        print(temp)
    elif i[0] == "pop_back":
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
    elif i[0] == "front":
        if len(que) > 0:
            temp = que[0]
        else:
            temp = -1
        print(temp)
    elif i[0] == "back":
        if len(que) > 0:
            temp = que[-1]
        else:
            temp = -1
        print(temp)
