n = input()
check = {}
cnt = 0
answer = ""
only_one = 1

for i in n.lower():
    try:  # 존재한다면 +1
        check[i] += 1
    except:  # 존재하지 않는다면 초기값 저장
        check[i] = 1


for j in check:
    if max(check.values()) == check.get(j):
        if cnt == 1:
            print("?")
            only_one = 0
            break
        cnt += 1
        answer += j


if only_one:
    print(answer.upper())
