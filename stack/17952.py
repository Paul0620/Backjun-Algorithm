# 17952 과제는 끝나지 않아 실4

from sys import stdin
from collections import deque

n = int(stdin.readline())
time = deque()
point = []
total = 0

for i in range(n):
    test = list(map(int, stdin.readline().split()))

    if test[0] == 1:
        point.append(test[1])
        time.append(test[2])
    else:
        pass

    if time:
        time[-1] -= 1
        if time[-1] == 0:
            time.pop()
            total += point.pop()

print(total)
