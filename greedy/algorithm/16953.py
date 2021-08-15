# A -> B 못푼 문제임**********************8
from sys import stdin
from collections import deque

a, b = map(int, stdin.readline().split())
s = ''
result = 0
que = deque()
que.append([a, 0])
cheker = 1
while que:
    temp = que.popleft()
    num, depth = temp
    if num == b:
        print(depth + 1)
        checker = 0
        break
    c1 = num * 2
    c2 = int(str(num) + '1')
    if c1 <= b:
        que.append([c1, depth + 1])
    if c2 <= b:
        que.append([c2, depth + 1])
if checker:
    print(-1)
