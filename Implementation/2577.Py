# 숫자의 개수
# 2577 브론즈2

answer = 1

for _ in range(3):
    temp = int(input())
    answer *= temp


temp_list = [0 for _ in range(10)]


for i in str(answer):
    if i == "0":
        temp_list[0] += 1
    elif i == "1":
        temp_list[1] += 1
    elif i == "2":
        temp_list[2] += 1
    elif i == "3":
        temp_list[3] += 1
    elif i == "4":
        temp_list[4] += 1
    elif i == "5":
        temp_list[5] += 1
    elif i == "6":
        temp_list[6] += 1
    elif i == "7":
        temp_list[7] += 1
    elif i == "8":
        temp_list[8] += 1
    elif i == "9":
        temp_list[9] += 1

for j in temp_list:
    print(j)
