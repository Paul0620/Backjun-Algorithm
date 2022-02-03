import math

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())

    f = math.ceil(n / h)
    print(f)
