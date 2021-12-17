# 이차원 배열 중복제거
arr = [[1, 2, 3, 4], [1, 2], [1, 3, 4]]
answer = []

# 가장 짧은 길이의 리스트를 맨 앞으로 가져옴
arr = sorted(arr)
# 짧은 길이의 리스트를 변수에 담는다
check = arr[0]

# 짧은 길이의 리스트의 값들 하나하나가 뒤의 리스트에 각각 존재하는지 확인
for i in check:
    is_check = True
    # 뒤의 리스트들을 하나 하나 돌며 값이 있는지 체크
    for j in range(1, len(arr)):
        # 하나의 리스트라도 없다면 False
        if i not in arr[j]:
            is_check = False

    # 모든 리스트에 해당 값이 존재한다면 추가
    if is_check:
        answer.append(i)

print(answer)
