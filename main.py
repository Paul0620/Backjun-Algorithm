# 효율적인 해킹
from sys import stdin
from collections import deque

def bfs(graph, start, visited):
    cnt = 0
    que = deque([start])
    visited[start] = True
    while que:
        v = que.popleft()
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True
    return cnt

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n+1)
temp = [[] for _ in range(n)]

for j in range(n):
    temp[j] = bfs(graph, j+1, visited)

for k in range(n):
    if temp[k] == max(temp):
        print(k+1, end=' ')


