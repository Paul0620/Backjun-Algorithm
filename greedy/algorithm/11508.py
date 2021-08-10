# 2+1 세일
import sys

n = int(sys.stdin.readline()) # 사람 수
t = [int(sys.stdin.readline()) for _ in range(n)] # 유제품 가격들
result = 0

t.sort(reverse=True) # 내림차순으로 정렬

for i in range(n):
  if (i+1) % 3 == 0: #배열 3의 배수 자리만 결과값에 합산하지 않는다.
    continue
  result += t[i]

print(result)