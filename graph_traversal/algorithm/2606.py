# 바이러스
from sys import stdin

def bsf(graph, start, visited):
    global cnt
    visited[start] = True # 방문한 노드는 True로
    for i in graph[start]: # 각 노드안에 연결된 값들을 꺼낸다
        if not visited[i]: # 해당 값이 이미 확인하였을 때 False라면
            bsf(graph, i, visited) # 재귀함수를 통하여 그 값을 확인
            cnt += 1 # 감염된걸로 확인했으니 증가

# 컴퓨터의 수
n = int(stdin.readline())
# 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
m = int(stdin.readline())
# 노드 번호의 시작이 1부터 시작하기 때문에 앞의 인덱스 0을 비워놓고 시작하기 위해 n + 1개만큼 리스트를 만든다
graph = [[] for _ in range(n + 1)]
# 쌍의 수 만큼 받아 graph에 넣는다
for _ in range(m):
    # 인덱스 번호를 노드번호와 맞추기 위해 공란을 두었으니 각 번호에 맞게 값을 담아준다
    # ex) 1 2 -> graph[1].append(2) 인덱스 1번에 값 2를 넣어준다
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0 # 바이러스에 걸리게 되는 컴퓨터 수
visited = [False] * (n + 1) # graph의 리스트 갯수만큼의 False 리스트를 만든다.

bsf(graph, 1, visited)

print(cnt)
