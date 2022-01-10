number = 0
answer = 0
temp = []
for i in range(1, 10):
    n = int(input())
    if n > answer:
        answer = n
        number = i

temp.append(answer)
temp.append(number)

for j in temp:
    print(j)
