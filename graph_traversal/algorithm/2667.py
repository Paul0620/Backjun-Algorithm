# 단지 번호 붙이기
from sys import stdin

def dfs(x, y):
    global cnt
    # graph의 범위를 벗어나거나 -1 보다 작다면 무시
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # x, y의 위치가 1이라면
    if graph[x][y] == 1:
        # 방문한 곳에 대해 1을 더해줌 나중에 또 체크 못하게
        graph[x][y] += 1
        # 집 카운트
        cnt += 1
        # 찾은 1 주변에 1이 있는지 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

n = int(stdin.readline())
graph = [list(map(int, stdin.readline().strip())) for _ in range(n)]

# 단지 수 카운트
result = 0
# 집의 수 카운트
cnt = 0
# 집의 수를 담아 놓을 리스트
temp = []

# graph for문 안에서 dfs를 수행하여 1을 찾아 단지 수 증가 그리고 집의 수를 temp에 담는다
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1
            temp.append(cnt)
            # 연결된 집들을 다 찾고나면 초기화 새로운 집들의 수를 카운트 하기 위해
            cnt = 0

print(result)
# 집의 수 오름차순 정렬
temp.sort()
for i in temp:
    print(i)