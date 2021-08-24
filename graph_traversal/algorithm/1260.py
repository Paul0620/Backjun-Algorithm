# DFS와 BFS
from sys import stdin
from collections import deque

# DFS 깊이 우선 탐색
def dfs(graph, start, visited):
    # visited start위치의 값 1을 0으로 바꾼다
    visited[start] = 0
    print(start, end=' ')
    for i in graph[start]:
        # 1이라면
        if visited[i]:
            # 재귀함수를 이용하여 검사
            dfs(graph, i, visited)

# BFS 너비 우선 탐색
def bfs(graph, start, visited):
    # 시간복잡도가 0(1)인 deque를 이용하여 처리한다
    que = deque([start])
    # visited start위치의 값 0을 1으로 바꾼다
    visited[start] = 1
    # que가 빌 때까지
    while que:
        # popleft()를 이용하여 앞에서부터 꺼낸다
        v = que.popleft()
        print(v, end=' ')
        for i in graph[v]:
            # 1이 아니라면
            if not visited[i]:
                que.append(i)
                visited[i] = 1

# 정점의 개수, 간선의 개수, 탐색을 시작할 번호
n, m, v = map(int, stdin.readline().split())
# 정점의 개수 + 1만큼 graph 리스트 만들기
graph = [[] * (n + 1) for _ in range(n + 1)]
# m개의 간선이 연결하는 두 정점의 번호를 받아 인덱스 == 번호의 위치에 값을 담는다
# ex) 3 4 -> graph[3].append(4) graph[4].append(3)
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

# graph의 수만큼 visited 리스트를 만든다
visited = [1] * (len(graph))

dfs(graph, v, visited)
print()
bfs(graph, v, visited)


# 또 다른 방식의 풀이
"""
# DFS와 BFS
from sys import stdin
from collections import deque

# DFS 깊이 우선 탐색
def dfs(graph, start, visited):
    # visited start위치의 값 0을 1으로 바꾼다
    visited[start] = 1
    # 방문한 곳에 대해서 출력
    print(start, end=' ')
    for i in range(1, n+1):
        # visited[i]의 값이 0이고 graph[start][i]의 값이 1이라면
        if visited[i] == 0 and graph[start][i] == 1:
            # 재귀함수를 이용하여 검사
            dfs(graph, i, visited)

# BFS 너비 우선 탐색
def bfs(graph, start, visited):
    # 시간복잡도가 0(1)인 deque를 이용하여 처리한다
    que = deque([start])
    # visited start위치의 값 1을 0으로 바꾼다
    visited[start] = 0
    # que가 빌 때까지
    while que:
        # popleft()를 이용하여 앞에서부터 꺼낸다
        v = que.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            # visited[i]가 1이고 graph[v][i]가 1이라면 que에 값을 추가
            if visited[i] == 1 and graph[v][i] == 1:
                que.append(i)
                visited[i] = 0

# 정점의 개수, 간선의 개수, 탐색을 시작할 번호
n, m, v = map(int, stdin.readline().split())
# 정점의 개수 + 1만큼 graph 리스트 만들기
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
# m개의 간선이 연결하는 두 정점의 번호를 받아 2차원 배열에 1로 담는다(자료가 있는 곳만 1)
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

# graph의 수만큼 visited 리스트를 만든다
visited = [0] * len(graph)

dfs(graph, v, visited)
print()
bfs(graph, v, visited)
"""