# 9012 괄호 실4

from collections import deque
from sys import stdin

n = int(input())

for _ in range(n):
    vps = stdin.readline().strip()
    que = deque()
    check = True

    if len(vps) % 2 == 1:
        print("NO")
        continue

    else:
        for i in range(len(vps)):
            if vps[i] == "(":
                que.append(i)
            elif vps[i] == ")":
                if que:
                    que.pop()
                else:
                    check = False
        if que or check == False:
            print("NO")
        else:
            print("YES")
