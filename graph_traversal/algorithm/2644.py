# 촌수계산
from sys import stdin
from collections import deque


# 전체 사람 수
n = int(stdin.readline())
# 촌수를 계산해야하는 서로 다른 사람의 번호
a, b = map(int, stdin.readline().split())
a -= 1
b -= 1
# 부모 자식의 관계의 개수
m = int(stdin.readline())

adj_list = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    adj_list[x-1][y-1] = 1
    adj_list[y-1][x-1] = 1

visit = [0 for _ in range(n)]

queue = deque()
# first in first out   ==  FIFO
queue.append([a, 0])
visit[a] = 1
answer = -1
while queue:
    temp, d = queue.popleft()
    if temp == b:
        answer = d
        break

    for i in range(n):
        if adj_list[temp][i] == 1 and visit[i] == 0:
            visit[i] = 1
            queue.append([i, d+1])

print(answer)