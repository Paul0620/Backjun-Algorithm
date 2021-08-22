# 효율적인 해킹
from sys import stdin
from collections import deque

# 각 노드에서 해킹가능 수를 리턴해준다
def bfs(graph, start):
    # 각 노드에서 해킹가능한 최대 수를 알아야하기 떄문에 bfs함수 사용마다 visited를 초기화 해준다
    visited = [False] * (n + 1)
    cnt = 0
    que = deque([start])
    visited[start] = True
    while que:
        v = que.popleft()
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True
    return cnt

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, stdin.readline().split())
    # 부모 노드에 자식 노드만 담는다
    # 부모가 자식을 신뢰하는지만 확인하면 되기때문
    graph[b].append(a)
temp = [[] for _ in range(n)]

# bfs에서 리턴받은 해킹가능 수를 temp에 담아준다
for j in range(n):
    temp[j] = bfs(graph, j+1)

# 각 노드의 해킹가능 수를 비교하여 최대 수 인것만 출력
for k in range(n):
    if temp[k] == max(temp):
        print(k+1, end=' ')