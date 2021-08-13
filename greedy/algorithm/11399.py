# ATM
import sys

n = int(sys.stdin.readline())  # 사람 수
t = list(map(int, sys.stdin.readline().split()))  # 인출하는데 걸리는 시간
temp = 0
result = 0

t.sort()  # 오름차순으로 정렬

for i in t:
    temp += i  # temp에 먼저 값과 새로운 값을 합해놓음
    result += temp  # 결과 값에 합한다

print(result)
