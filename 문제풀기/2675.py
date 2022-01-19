n = int(input())

for _ in range(n):
    answer = ""
    r, s = input().split()

    for i in s:
        answer += i * int(r)
    print(answer)
