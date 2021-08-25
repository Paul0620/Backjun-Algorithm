# 토마토
from sys import stdin
from collections import deque

# BFS를 이용해 토마토가 며칠만에 다 익는지 확인한다


def bfs(que):
    global days
    while que:
        # 시간복잡도가 O(1)인 deque의 popleft()함수를 이용하여 첫번째 값을 가져온다.
        x, y, depth = que.popleft()
        # 시작값 주변에 찾기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 안에 있다면
            if 0 <= nx < n and 0 <= ny < m:
                # 주변에 0(안익은 토마토)가 있다면 1로 바꾸고 날짜를 1증가
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    que.append([nx, ny, depth + 1])
                    days = depth + 1
    return days


m, n = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
que = deque()
# 상, 하, 좌, 우를 위한 값
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 날짜 초기값 설정
days = 0
# 안익은 토마토 체크를 위한 값 설정
check = 0

# deque함수를 이용하여 que에 익은 토마토를 찾아 그 위치와 시작값을 담는다
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            que.append([i, j, 0])

# BFS에 que에 담은 값을 보낸다
bfs(que)

# 다른 토마토들이 익은토마토의 영향을 받았는지 확인하여 0이 있다면 check를 1로 바꾼다
for i in graph:
    if 0 in i:
        check = 1
        break

# 토마토가 다 익지 않았다면 -1 출력
if check:
    print(-1)
# 다 익었다면 며칠만에 다익었는지 출력
else:
    print(days)
