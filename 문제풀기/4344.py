c = int(input())
for _ in range(c):
    case = list(map(int, input().split()))
    n = case[0]
    avg = sum(case[1 : n + 1]) / n
    temp = []

    for i in range(1, n + 1):
        if case[i] > avg:
            temp.append(case[i])

    answer = len(temp) / len(case[1 : n + 1]) * 100

    print("%0.3f%%" % answer)
