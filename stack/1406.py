# 1406 에디터 실3

from sys import stdin

n = list(stdin.readline().strip())
m = int(stdin.readline())
cnt = len(n)
temp = []

for _ in range(m):
    order = stdin.readline().split()

    if order[0] == "L" and n:
        temp.append(n.pop())

    elif order[0] == "D" and temp:
        n.append(temp.pop())

    elif order[0] == "B" and n:
        n.pop()

    elif order[0] == "P":
        n.append(order[1])

print("".join(n + list(reversed(temp))))
