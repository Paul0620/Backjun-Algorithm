# 1316 그룹 단어 체커 실5

n = int(input())
input_list = []
cnt = 0

for _ in range(n):
    temp = input()
    input_list.append(temp)

for i in input_list:
    temp_list = []
    for j in range(len(i)):
        if i[j] not in temp_list or i[j] == i[j - 1]:
            temp_list.append(i[j])

        if len(temp_list) == len(i):
            cnt += 1

print(cnt)
