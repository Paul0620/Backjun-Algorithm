# 2346 풍선 터뜨리기 실3

from collections import deque

n = int(input())
que = deque([(index, value) for index, value in enumerate(map(int, input().split()))])
answer = []

while que:
    a = que.popleft()
    answer.append(a[0] + 1)

    if que and a[1] > 0:
        que.rotate(-(a[1] - 1))
    else:
        que.rotate(-a[1])

for i in answer:
    print(i, end=" ")
