from sys import stdin

n = int(input())
temp_list = []

for i in range(n):
    temp = stdin.readline().strip()
    temp = temp.replace("\n", "")
    if temp not in temp_list:
        temp_list.append(temp)

temp_list = sorted(temp_list)
temp_list = sorted(temp_list, key=lambda x: len(x))

for i in temp_list:
    print(i)
