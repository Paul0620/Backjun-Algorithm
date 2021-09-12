# 봄버맨
from sys import stdin
from collections import deque

# 폭탄 위치 찾기
def search_bombs():
    for x in range(r):
        for y in range(c):
            # 해당 좌표에 폭탄 'O'이 있다면 deque에 담아준다
            if graph[x][y] == 'O':
                que.append((x, y))

# 빈공간을 폭탄으로 채워주기
def make_bombs():
    for x in range(r):
        for y in range(c):
            # 해당 좌표가 빈공간 '.'이라면 폭탄으로 바꿔준다
            if graph[x][y] == '.':
                graph[x][y] = 'O'

# 폭발
def explosion():
    # 초기 폭탄 위치값을 담아둔 que를 이용
    while que:
        # popleft를 이용하여 값을 꺼내 폭탄위치와 상, 하, 좌, 우의 방향을 터트려 '.'로 바꿔준다.
        x, y = que.popleft()
        graph[x][y] = '.'
        if 0 <= x - 1:
            graph[x - 1][y] = '.'
        if x + 1 < r:
            graph[x + 1][y] = '.'
        if 0 <= y - 1:
            graph[x][y - 1] = '.'
        if y + 1 < c:
            graph[x][y + 1] = '.'

r, c, n = map(int, stdin.readline().split())
graph = [list(stdin.readline().strip()) for _ in range(r)]
que = deque()
# 처음 1초에는 변화없이 그대로이기 때문에 -1 해준다.
n -= 1
# 남은 시간만큼 while문을 동작한다.
while n:
    search_bombs()
    make_bombs()
    # 폭탄을 찾고 폭탄으로 채워줬다면 1초 감소
    n -= 1
    # 만약 초가 0초라면 탈출
    if n == 0:
        break
    explosion()
    # 폭탄이 터지고 나서 1초 감소
    n -= 1

# while문 탈출 후 현재 graph 상태 출력
for i in graph:
    print(''.join(i))