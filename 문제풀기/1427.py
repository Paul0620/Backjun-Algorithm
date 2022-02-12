n = input()

temp = sorted(n, reverse=True)
answer = ""

for i in temp:
    answer += i

print(int(answer))
