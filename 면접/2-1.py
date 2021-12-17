# 팰린드롬 초기 값을 문자로 받음
left = "4"
right = "1000"
cnt = 0

# 초기값을 문자로 받기 때문에 정수형으로 변환
left = int(left)
right = int(right)

# +1을 하는 이유는 4~1000의 범위까지가 포함이기 때문 for문은 0부터 시작이라 999까지 나오게 됨
for num in range(left, right + 1):
    # 숫자의 왼쪽 오른쪽이 같은지 확인하기 위해 문자열로 바꿔줌
    sNum = str(num)
    # 슈퍼 펠린드롬을 찾아야 하기 때문에 루트를 곱하여 나온 값을 변수에 담아 문자열로 변환
    hNum = str(num ** 0.5)

    # 루트값이 딱 떨어졌을 때 뒤에 '.0'으로 나오기 때문에 두 조건을 만족한 값들만 실행하도록
    if hNum[-1] == '0' and hNum[-2] == '.':
        # 조건에 맞는 수는 '.0'을 제거하여 문자열로 변환
        hNum = str(int(float(hNum)))
        # 문자가 일치하는지 체크를 하기 위한 변수
        is_check = True
        for j in range(len(sNum) // 2):
            # 주어진 값과 그 값의 루트 값이 양쪽 문자가 일치하는지 확인 하나라도 일치하지 않는다면 False
            if sNum[j] != sNum[-1 - j] or hNum[j] != hNum[-1 - j]:
                is_check = False

        # 두 가지 조건을 다 통과했을 때 cnt + 1처리
        if is_check:
            cnt += 1

print(cnt)
