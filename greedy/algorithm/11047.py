# 동전 0
from sys import stdin

N, K = map(int, stdin.readline().split())
coins = []
result = 0

for _ in range(N): # 동전의 가치들을 리스트로 담는다
    coins.append(int(stdin.readline()))

coins.sort(reverse=True) # 내림차순으로 정렬

for coin in coins: 
    result += K // coin # result에 결과값 개수 담기
    K %= coin # 나머지 금액을 K에 담기

print(result)