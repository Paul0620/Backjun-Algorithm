t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())

    if n % h == 0:
        floor = h
        line = n // h
    else:
        floor = n % h
        line = n // h + 1

    answer = floor * 100 + line

    print(answer)
