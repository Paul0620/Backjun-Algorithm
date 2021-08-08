# 주유소
import sys

n = int(input())  # 도시 개수
road = list(map(int, sys.stdin.readline().split()))  # 각 도시간의 거리
cities = list(map(int, sys.stdin.readline().split()))  # 각 도시의 리터당 기름값
result = 0  # 결과값 담을 변수
s = cities[0]  # 초기 기름값 변수에 담기

for i in range(len(cities)-1):  # 맨 마지막 도시는 반영할 필요가 없다.
  if s >= cities[i]:  # 초기 기름값이 새로운 기름값보다 크거나 같다면
    s = cities[i]  # 새로운 기름값을 담기
  result += s * road[i]  # 기름 * 거리 값을 result에 담기

print(result)
