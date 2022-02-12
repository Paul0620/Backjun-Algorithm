from sys import stdin

n = int(input())
temp_list = []

for _ in range(n):
    temp = list(map(int, stdin.readline().split()))
    temp_list.append(temp)

temp_list = sorted(temp_list)

for i in temp_list:
    print(f"{i[0]} {i[1]}")
