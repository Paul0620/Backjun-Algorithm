n = int(input())
cnt = 0

for i in range(1, n + 1):
    if i < 100:
        cnt += 1
    else:
        temp = str(i)
        if int(temp[1]) - int(temp[0]) == int(temp[2]) - int(temp[1]):
            cnt += 1

print(cnt)
