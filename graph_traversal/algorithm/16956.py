# 늑대와 양
from sys import stdin

# 늑대 주변이 양인지 빈공간인지 확인
def bfs(x, y):
    for k in range(4):
        nx, ny = dx[k] + x, dy[k] + y
        if 0 <= nx < r and 0 <= ny < c:
            if feild[nx][ny] == 'S':
                return False
            elif feild[nx][ny] == '.':
                feild[nx][ny] = 'D'
    return True

# 목장 크기
r, c = map(int, stdin.readline().split())
# 목장 상태를 받음
feild = [list(stdin.readline().strip()) for _ in range(r)]

# 이동방향(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# feild에서 늑대를 찾아 bfs함수를 통해 return값을 받는다
for i in range(r):
    for j in range(c):
        check = True
        if feild[i][j] == 'W':
            check = bfs(i, j)
            if check == False:
                print(0)
                break

if check:
    print(1)
    for i in feild:
        print(''.join(i))