# 토마토
from sys import stdin
from collections import deque

def bfs(x, y):
    que = deque([(x, y)])
    global result
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or x < nx or ny < 0 or y < ny:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                result += 1
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx, ny))
    return graph[n - 1][m - 1]

m, n = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
result = 0

# 0이 하나도 없고 1이 한개 이상 있다면 -> 0 출력
# -1이 있거나 없거나 길이 있고 최종 좌표까지 갈 수 있다면 모든 0을 1로 바꾸는데 걸리는 카운트 수 출력

# -1로 인해 길이 막혀 0을 1로 바꿀 수 없다면 -> -1 출력
for i in graph:
    if 0 not in i:
        cnt += 1
if cnt == len(graph):
    print(-1)

#for i in range(n):
 #   for j in range(m):

  #      if graph[i][j] ==



from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(m)]
checker = 1
cnt = 0
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
que = deque()
for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            que.append([i, j, 0])
answer = 0
while que:
    i, j, depth = que.popleft()
    for a in range(4):
        ni = i + di[a]
        nj = j + dj[a]
        if 0 <= ni < m and 0 <= nj < n:
            if arr[ni][nj] == 0:
                arr[ni][nj] = 1
                que.append([ni, nj, depth+1])
                answer = depth + 1
in_zero = 0
for line in arr:
    if 0 in line:
        in_zero = 1
        break
if in_zero:
    print(-1)
else:
    print(answer)