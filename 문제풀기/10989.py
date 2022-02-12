from sys import stdin

n = int(stdin.readline())
temp_list = {}

for _ in range(n):
    temp = int(stdin.readline())
    if temp not in temp_list:
        temp_list[temp] = 1
    else:
        temp_list[temp] += 1

temp_list = sorted(temp_list.items())

for i in temp_list:
    for _ in range(i[1]):
        print(i[0])
