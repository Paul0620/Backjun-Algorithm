# 봄버맨
from sys import stdin
from collections import deque

r, c, n = map(int, stdin.readline().split())
graph = [list(stdin.readline().strip()) for _ in range(r)]
que = deque()

if n == 1 or (4 <= n and n % 2 != 0):
    for i in graph:
        print(''.join(i))
elif n == 2 or (4 <= n and n % 2 == 0):
    for _ in range(r):
        print('OOOOOOO')
else:
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'O':
                que.append((i, j))
            elif graph[i][j] == '.':
                graph[i][j] = 'O'


    while que:
        x, y = que.popleft()
        graph[x][y] = '.'
        if 0 <= x - 1:
            graph[x - 1][y] = '.'
        if x + 1 < r:
            graph[x + 1][y] = '.'
        if 0 <= y - 1:
            graph[x][y - 1] = '.'
        if y + 1 < c:
            graph[x][y + 1] = '.'

    for i in graph:
        print(''.join(i))
