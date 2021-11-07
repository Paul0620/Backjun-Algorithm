# 숨박꼭질
from collections import deque

# 수빈이 위치 n, 동생 위치 k
n, k = map(int, input().split())
r = 100000


def is_valid(temp):
    if 0 <= temp <= r and graph[temp] == 0:
        return True
    else:
        return False


# 필드 범위
graph = [0 for _ in range(r+1)]

que = deque()
que.append([n, 0])
graph[n] = 1
answer = 0

while que:
    temp, d = que.popleft()
    nexts = [temp+1, temp-1, temp*2]

    if temp == k:
        answer = d
        break

    for nex in nexts:
        if is_valid(nex):
            graph[nex] = 1
            que.append([nex, d+1])

print(answer)
