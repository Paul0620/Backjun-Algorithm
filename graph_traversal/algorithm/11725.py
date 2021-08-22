# 트리의 부모 찾기
from sys import stdin
from sys import setrecursionlimit

# DFS 깊이 우선 탐색
def dfs(graph, start, parents):
    # graph[노드번호] 위치에 있는 값들을 꺼내온다
    for i in graph[start]:
        # 0이라면
        if parents[i] == 0:
            # parents[i] 위치에 부모 노드를 담아준다.
            parents[i] = start
            # 재귀 함수를 통해 해당 노드의 값들을 확인
            dfs(graph, i, parents)

# 노드의 개수
n = int(stdin.readline())
# n-1개의 줄에 트리 상에서 연결된 두 정점을 받음
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
# 부모의 노드를 담을 리스트
parents = [0] * len(graph)
# 런타임에러(RecursionError)방지 - 최대 재귀 깊이를 변경
setrecursionlimit(10**6)

dfs(graph, 1, parents)

# parents에 담은 부모 노드를 출력
for i in range(2, n+1):
    print(parents[i])