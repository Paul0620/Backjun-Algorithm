n = int(input())

for _ in range(n):
    case = input()
    cnt = 0
    total = 0

    for i in case:
        if i == "O":
            cnt += 1
        else:
            cnt = 0

        total += cnt

    print(total)
