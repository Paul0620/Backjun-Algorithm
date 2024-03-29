# DFS(Depth-First Search) 깊이 우선 탐색
# 깊은 부분을 우선적으로 탐색
# 스택 자료구조 혹은 재귀 함수를 사용
# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
# 2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리.
#    방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복

# 방문기준(시작노드)는 문제에 따라 다름


def dfs(graph, v, visited):
    visited[v] = True  # 방문 체크 표시를 위해 True로 선언
    print(v, end=" ")  # 띄어쓰기 간격으로 방문 노드 순서 출력

    for i in graph[v]:  # 해당 노드에 담긴 연결 노드값을 for을 통해 하나씩 가져온다
        if not visited[i]:  # 방문한 노드가 아니라면 진행
            dfs(graph, i, visited)


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

dfs(graph, 1, visited)  # 노드 연결 정보, 시작 노드 번호, 방문 리스트
