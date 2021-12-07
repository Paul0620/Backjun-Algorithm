# 1874 스택 수열 실3

from sys import stdin

n = int(input())
cnt = 0
temp_list = []
cal_list = []
no = True

for _ in range(n):
    temp = int(stdin.readline())

    while cnt < temp:  # 입력받는 값만큼 temp_list에 cnt값을 넣어줌
        cnt += 1
        # while문 탈출할때까지 수와 +를 각각 리스트에 담음
        temp_list.append(cnt)  # 수를 담는 리스트
        cal_list.append("+")  # +, -를 담는 리스트

    if temp_list[-1] == temp:  # temp_list의 마지막 값이 입력받은 temp값과 같다면
        temp_list.pop()  # 그 값을 제거
        cal_list.append("-")  # cal_list에 - 추가
    else:  # 불가능할 경우 True값을 False로 변경
        no = False
        break

if no == False:
    print("NO")
else:
    print("\n".join(cal_list))
