# 블로그2
import sys

n = int(sys.stdin.readline())
color = sys.stdin.readline().strip()
result = 1
r = b = 0

for i in color.split('R'):
    if 'B' in i:
        b += 1

for j in color.split('B'):
    if 'R' in j:
        r += 1

if b > r:
    result += r
else:
    result += b

print(result)
