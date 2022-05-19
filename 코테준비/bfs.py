# BFS(Breadth-First Search) 너비 우선 탐색, 가까운 노드부터 우선적으로 탐색
# 큐 자료구조를 이용
# 1. 탐색 시작 노드를 큐에 삽입하고 방문처리
# 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
# 3. 더 이상 2번의 과정을 수핼할 수 없을 때까지 반복

from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])  # 큐 구현을 위해 deque를 사용, que에 노드를 담는다
    visited[start] = True  # 노드 방문처리

    # queue에 노드가 없어질 때까지 while문을 통해 동작
    while queue:
        v = queue.popleft()  # 큐에서 값 하나를 빼기, 먼저 들어온 값
        print(v, end=" ")

        for i in graph[v]:
            if not visited[i]:  # 방문하지 않은 노드라면
                queue.append(i)  # 노드를 큐에 담아준다
                visited[i] = True  # 해당노드 방문처리


# 2차원 리스트 형식의 노드 연결 정보
graph = [
    [],  # 비워두는 이유는 노드 번호가 1부터 시작이라, 리스트의 인덱스는 0번부터 시작
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

# 각 노드의 방문체크를 확인하기 위한 1차원 리스트, 9칸으로 만든 이유는 인덱스 0을 사용하지 않기 때문
visited = [False] * 9

bfs(graph, 1, visited)  # 노드 연결 정보, 시작 노드 번호, 방문 리스트
