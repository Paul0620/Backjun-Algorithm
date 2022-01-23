a, b, c = map(int, input().split())

if b >= c:
    answer = -1
else:
    temp = c - b
    answer = a // temp + 1

print(answer)
