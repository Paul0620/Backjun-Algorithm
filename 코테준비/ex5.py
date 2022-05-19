# 문제푼거
from itertools import combinations

def solution(nums):
    answer = 0
    temp = list(combinations(nums, 3)) # combimations를 활용한 숫자 조합 리스트
    temp_list = [] # 서로 다른 3개의 숫자 조합

    # 조합한 숫자의 합계를 temp_list에 담는다
    for t in temp:
        temp_list.append(sum(t))

    # temp_list에 있는 각 숫자 합을 하나씩 가져와 소수찾기
    for i in temp_list:
        check = False
        for j in range(2, i):
            if i % j == 0: # 2부터 i - 1숫자까지 0으로 나눠지는 숫자가 있다면
                check = True # True 바꾸기

        if not check: # False라면 소수 개수 추가
            answer += 1

    return answer


def solution(v):
    answer = []
    x_list = []
    y_list = []

    for x, y in v:
        # x_list안에 좌표 x값이 없다면 넣어준다
        if x not in x_list:
            x_list.append(x)
        else: # x값이 있다면 제거해준다(짝이 맞는 좌표를 찾기위해 짝이 맞는다면 제거)
            x_list.remove(x)
        # y좌표도 x좌표와 같은 방법으로
        if y not in y_list:
            y_list.append(y)
        else:
            y_list.remove(y)

    answer = x_list + y_list
    
    return answer