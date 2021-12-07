# 10773 제로 실4

from collections import deque
from sys import stdin

n = int(input())
que = deque()

for _ in range(n):
    temp = int(stdin.readline())
    if temp != 0:
        que.append(temp)
    else:
        que.pop()


print(sum(que))
