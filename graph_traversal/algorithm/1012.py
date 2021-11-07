# 유기농 배추
from collections import deque

# 테스트 케이스 개수
t = int(input())

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 출력할 답 리스트
answer_list = []

# 테스트 케이스 수 만큼 케이스 별로 탐색
for _ in range(t):
    m, n, k = map(int, input().split())  # 가로, 세로, 배추 위치개수
    cnt = 0  # 지렁이 개수
    graph = [[0 for _ in range(m)] for _ in range(n)]  # 필드 생성

    # 배추가 있는 위치에 1로 값 변경
    for _ in range(k):
        x, y = map(int, input().split())  # m, n
        graph[y][x] = 1  # y열의 x행 위치에 값을 담음

    que = deque()

    # 좌표별로 탐색하며 배추가 있다면 지렁이 개수를 1증가 시키고 0으로 변환
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt += 1
                que.append([i, j])
                graph[i][j] = 0
                # 배추가 있는 위치의 4방향에 배추가 있다면 같이 0으로 변환
                while que:
                    y, x = que.popleft()  # y열의 x행 위치 값을 가져옴
                    for k in range(4):
                        nx = x + dx[k]  # m
                        ny = y + dy[k]  # n
                        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                            graph[ny][nx] = 0
                            que.append([ny, nx])

    answer_list.append(cnt)

for answer in answer_list:
    print(answer)
