# 에너지 드링크
import sys

n = int(sys.stdin.readline()) # 드링크 수
t = list(map(int, sys.stdin.readline().split())) # 각 드링크의 양
result = 0

t.sort(reverse=True) # 내림차순으로 정렬

for i in range(n):
  if i == 0: # 배열 첫번째 값만 그대로 넣어줌
    result += t[i]
  else: # 배열 두번째 값부터는 / 2하여 넣어준다.
    result += t[i] / 2


print("%g" %result)