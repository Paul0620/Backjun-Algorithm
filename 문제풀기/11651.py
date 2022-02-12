from sys import stdin

n = int(input())
temp_list = []

for _ in range(n):
    a, b = map(int, stdin.readline().split())
    temp_list.append([b, a])

temp_list = sorted(temp_list)

for i in temp_list:
    print(f"{i[1]} {i[0]}")
