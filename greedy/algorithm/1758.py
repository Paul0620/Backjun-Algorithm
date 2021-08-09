# 알바생 강호
import sys

n = int(sys.stdin.readline())  # 손님수
tip = [int(sys.stdin.readline()) for _ in range(n)]  # 손님 팁 받기
result = 0
tip.sort(reverse=True)  # 최대값을 구하는 것이라 제일 높은 팁순으로 정렬

for i in range(n):
  if tip[i] - ((i+1)-1) > 0:  # 팁 금액이 0보다 크다면 result에 반영
    result += tip[i] - ((i+1)-1)

print(result)