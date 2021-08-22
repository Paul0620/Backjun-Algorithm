# 꿀 따기 - 55점 나옴 만점 아님.
from sys import stdin

n = int(stdin.readline())
h = list(map(int, stdin.readline().split()))


temp_a = []
temp_b = []
result = []
temp = sum(h[1:])
for i in range(1, n):
    temp_a.append(temp - h[i])
    temp_b.append(sum(h[i:]) - h[i])
result.append(max([a + b for a, b in zip(temp_a, temp_b)]))

temp_a = []
temp_b = []
h.reverse()
temp = sum(h[1:])
for i in range(1, n):
    temp_a.append(temp - h[i])
    temp_b.append(sum(h[i:]) - h[i])
result.append(max([a + b for a, b in zip(temp_a, temp_b)]))

temp_a = []
temp_b = []
cnt = len(h) // 2 + 1
temp_a = (sum(h[1:cnt]))
h.reverse()
temp_b = (sum(h[1:cnt]))
result.append(temp_a + temp_b)

print(max(result))
