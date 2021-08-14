# 블로그2
import sys

n = int(sys.stdin.readline())
color = sys.stdin.readline().strip()
result = 1 # 초기 값을 1로 받음 전체를 한번 색칠하기 위해서
r = b = 0

for i in color.split('R'): # split으로 분리해 각 문자의 갯수가 아닌 붙어있는 것이 하나로 쳐서 카운트
    if 'B' in i:
        b += 1

for j in color.split('B'):
    if 'R' in j:
        r += 1

if b > r: # 더 적은 색의 값만 초기값에 더하면 끝
    result += r
else:
    result += b

print(result)
