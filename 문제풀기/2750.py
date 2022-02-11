n = int(input())
temp_list = []

for _ in range(n):
    temp = int(input())
    temp_list.append(temp)

temp_list = sorted(temp_list)

for i in temp_list:
    print(i)
