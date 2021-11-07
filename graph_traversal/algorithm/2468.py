# 안전영역
from collections import deque

# 2차원 배열 수
n = int(input())


def is_valid(x, y, n):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False


# 2차원 배열 값 담기
graph = []
maximum = 0
for c in range(n):
    graph.append(list(map(int, input().split())))
    t = max(graph[c])
    if maximum < t:
        maximum = t


# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
# 안전 영역 지대 수
cnt = 0
for h in range(maximum):
    temp = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and visited[i][j] == 0:
                temp += 1
                queue.append([i, j])
                visited[i][j] = 1
                # bfs 탐색을 할거에용~~
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if is_valid(nx, ny, n) and visited[nx][ny] == 0 and graph[nx][ny] > h:
                            visited[nx][ny] = 1
                            queue.append([nx, ny])
    if temp > cnt:
        cnt = temp

print(cnt)
