"""
n * (n + 1) // 2
"""

n = int(input())
cnt = 0
temp_list = []

while True:
    cnt += 1
    x = cnt * (cnt + 1) // 2
    if n <= x:
        break

if cnt % 2 != 0:
    a = cnt
    b = 1
    for _ in range(cnt):
        temp = str(a) + "/" + str(b)
        temp_list.append(temp)
        a -= 1
        b += 1
else:
    a = 1
    b = cnt
    for _ in range(cnt):
        temp = str(a) + "/" + str(b)
        temp_list.append(temp)
        a += 1
        b -= 1

c = 0

for i in range(1, cnt):
    c += i

answer = n - c

print(temp_list[answer - 1])
