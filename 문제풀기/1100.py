cnt = 0

for i in range(8):
    n = input()
    if i % 2 == 0:
        for j in range(len(n)):
            if j % 2 == 0 and n[j] == "F":
                cnt += 1

    else:
        for j in range(len(n)):
            if j % 2 != 0 and n[j] == "F":
                cnt += 1

print(cnt)
