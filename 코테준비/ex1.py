# 음료수 얼려 먹기

n = 4
m = 5
graph = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

result = 0

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    # 주어진 범위를 벗어난다면 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1  # 해당 노드를 방문처리
        # dfs(x - 1, y)
        # dfs(x, y - 1)
        # dfs(x + 1, y)
        # dfs(x, y + 1)
        for h in range(4):  # 4방향에 연결된 노드가 있는 범위까지 재귀함수를 통해 방문 처리한다
            dfs(x + dx[h], y + dy[h])
        return True
    return False


for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS를 수행한다
        if dfs(i, j) == True:
            result += 1

print(result)
