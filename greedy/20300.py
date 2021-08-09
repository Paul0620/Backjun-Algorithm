#서강근육맨
import sys

n = int(sys.stdin.readline()) # 운동기구 개수
t = list(map(int, sys.stdin.readline().split())) # 근손실 정도
arr = []
result = 0
t.sort() # 내림차순으로 정렬

if n % 2 == 0: # 운동기구 개수가 짝수라면
  for i in range(n // 2): # 하루에 2개씩 운동하니 n // 2
    s = t[i] + t[-(i+1)] # 제일 큰값 + 제일 작은 값을 더함
    arr.append(s) # 더한 값을 arr에 담는다
  result = max(arr) # 최솟값이니 그 합계중 가장 큰값이 최솟값이 된다.
else:
  result = t[-1] # 홀수의 경우라 가장 큰값을 미리 담아둔다
  for i in range(n // 2):
    s = t[i] + t[-(i+2)]
    arr.append(s)
  if result < max(arr): # 담아놓은 배열의 최솟값이 result보다 크다면
    result = max(arr) # 결과값을 바꿔준다

print(result)