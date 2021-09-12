# 봄버맨
from sys import stdin
from collections import deque

def search_bombs():
    for x in range(r):
        for y in range(c):
            if graph[x][y] == 'O':
                que.append((x, y))

def make_bombs():
    for x in range(r):
        for y in range(c):
            if graph[x][y] == '.':
                graph[x][y] = 'O'

def explosion():
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

r, c, n = map(int, stdin.readline().split())
graph = [list(stdin.readline().strip()) for _ in range(r)]
que = deque()
n -= 1
while n:
    search_bombs()
    make_bombs()
    n -= 1
    if n == 0:
        break
    explosion()
    n -= 1

for i in graph:
    print(''.join(i))