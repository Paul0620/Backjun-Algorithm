# 10799 쇠막대기 실3

n = input()
check = []
cnt = 0
bar = 0

n = n.replace("()", "0")

for i in n:
    if i == "(":
        cnt += 1
        bar += 1
    elif i == "0":
        cnt += bar
    else:
        bar -= 1

print(cnt)
