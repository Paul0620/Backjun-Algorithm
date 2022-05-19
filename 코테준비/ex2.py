# 미로탈출
from collections import deque

n = 5
m = 6

graph = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    que = deque()
    que.append((x, y))  # 큐에 시작 좌표값을 담아준다

    while que:
        x, y = que.popleft()

        # 현재 좌표에서 4방향의 위치 확인, 연결되어있는 길을 찾기 위해
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 그래프 범위를 벗어난경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:  # 만약 막혀있는 길이라면
                continue

            if graph[nx][ny] == 1:  # 연결되어 있는 길이라면
                graph[nx][ny] = graph[x][y] + 1  # 이전 좌표에 값에 +1을 하여 다음 진행할 노드에 선언
                que.append((nx, ny))  # 큐에 다음 방향이될 좌표값을 담는다

    return graph[n - 1][m - 1]  # 가장 오른쪽 아래까지의 최단 거리 반환


print(bfs(0, 0))  # 시작 좌표값
