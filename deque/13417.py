# 13417 카드 문자열 실3 아직 해결못함

from collections import deque

n = int(input())
an_list = []

for _ in range(n):
    cnt = int(input())
    s_list = deque(input().split())
    answer = deque()

    while s_list:
        if not answer:
            a = s_list.popleft()
            answer.append(a)

        elif a > s_list[0]:
            answer.appendleft(s_list.popleft())

        else:
            answer.append(s_list.popleft())

    an_list.append("".join(answer))

for j in range(len(an_list)):
    print(an_list[j])
