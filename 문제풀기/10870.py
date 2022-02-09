n = int(input())
cnt = 0
answer = 0
f = 0
s = 1

while True:

    if cnt == n:
        print(answer)
        break
    if cnt >= 1:
        answer = f + s
        f = s
        s = answer
    else:
        answer += 1

    cnt += 1
