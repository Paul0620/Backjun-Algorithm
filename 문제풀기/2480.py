n = list(map(int, input().split()))
temp = {}
cnt = 0
answer = 0

for i in n:
    if i not in temp:
        temp[i] = 1
    else:
        temp[i] += 1

k_temp = dict(zip(temp.values(), temp.keys()))

if len(temp) == 1:
    answer += 10000 + (n[0] * 1000)
elif len(temp) == 2:
    answer += 1000 + (k_temp.get(max(k_temp)) * 100)
elif len(temp) == 3:
    answer += max(n) * 100

print(answer)
