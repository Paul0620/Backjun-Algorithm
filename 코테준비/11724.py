# 연결 요소의 개수
from collections import deque

n, m = map(int, input().split())

answer = 0

graph = [[0 for _ in range(n)] for _ in range(n)]
visited = [0 for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

que = deque()

for i in range(n):
    if visited[i] == 0:
        que.append(i)
        visited[i] = 1

        while que:
            t = que.popleft()

            for j in range(n):
                if graph[t][j] == 1 and visited[j] == 0:
                    que.append(j)
                    visited[j] = 1

        answer += 1

print(answer)
