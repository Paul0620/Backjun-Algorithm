# 미로 탐색
from sys import stdin
from collections import deque

# 최소이동 칸수를 구한다
def bfs(x, y):
    que = deque()
    que.append((x, y))
    # 큐가 빌 때가지 반복
    while que:
        x, y = que.popleft()
        # 현재 위치에서 네 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 0보다 작거나, graph의 범위를 벗어난다면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽을 만났으면 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 위치를 처음 방문한 경우에 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx, ny))
    return graph[n - 1][m - 1]

n, m = map(int, stdin.readline().split())
# 2차원 리스트의 맵 정보 입력받기
graph = [list(map(int, stdin.readline().strip())) for _ in range(n)]
# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 시작값 입력하여 결과 출력
print(bfs(0, 0))