# 1021 회전하는 큐 실4

from collections import deque

n, m = map(int, input().split())
que = deque(i + 1 for i in range(n))
temp_list = list(map(int, input().split()))
cnt = 0

for j in temp_list:
    while True:
        if que.index(j) == 0:
            que.popleft()
            break

        elif que.index(j) >= len(que) - que.index(j):
            que.rotate(1)
            cnt += 1

        else:
            que.rotate(-1)
            cnt += 1

print(cnt)
