n = int(input())
temp_list = []

for _ in range(n):
    age, name = input().split()
    temp_list.append([int(age), name])

temp_list = sorted(temp_list, key=lambda x: x[0])

for i in temp_list:
    print(f"{i[0]} {i[1]}")
