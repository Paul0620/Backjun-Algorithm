t = int(input())

for _ in range(t):
    k = int(input())  # 층
    n = int(input())  # 호

    # 0층
    floor_list = [i for i in range(1, n + 1)]

    for j in range(k):
        for h in range(1, n):
            floor_list[h] += floor_list[h - 1]
    print(floor_list[-1])
