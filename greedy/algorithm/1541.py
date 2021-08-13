# 잃어버린 괄호
import sys

n = sys.stdin.readline().strip().split('-')  # 입력받을때 -를 기준으로 -제거하고 리스트로 만듬
arr = []
result = 0

for i in n:
    temp = 0
    for j in i.split('+'):  # 문자 +를 제거후 그 값들끼리 합하여 arr에 담아준다.
        temp += int(j)
    arr.append(temp)

result += int(arr[0])  # 첫번째 값을 미리 담아놓음

for i in range(1, len(arr)):  # 두번째 값부터 시작
    result -= arr[i]

print(result)
