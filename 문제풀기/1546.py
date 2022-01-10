n = int(input())
grades = list(map(int, input().split()))
m = max(grades)
temp = []

for i in grades:
    temp.append(i / m * 100)

print(sum(temp) / len(temp))
