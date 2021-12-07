# 2108 통계학 실4

import collections
from sys import stdin

n = int(input())
n_list = []
cnt = 0

for _ in range(n):
    temp = int(stdin.readline())
    n_list.append(temp)

avg = round(sum(n_list) / len(n_list))
mid = sorted(n_list)[(len(n_list) // 2)]

counters = collections.Counter(sorted(n_list)).most_common()

if n > 1:
    # 둘다 음수일 경우 반대로 2번째가 아닌 첫번째 값을 챙김
    if counters[0][1] < 0 and counters[1][1] < 0:
        if counters[0][1] == counters[1][1]:
            cnt = counters[0][0]
        else:
            cnt = counters[1][0]
    else:
        if counters[0][1] == counters[1][1]:
            cnt = counters[1][0]
        else:
            cnt = counters[0][0]

else:
    cnt = counters[0][0]

gap = max(n_list) - min(n_list)

print(avg)
print(mid)
print(cnt)
print(gap)
