# 연속되는 자연수의 합이 k와 같은 경우의 수
arr = [1, 1, 0, -1, 1]
# arr = [1, 1, 1, 1]
# arr = [1, 2, -1, 3]
k = 2
cnt = 0

for i in range(len(arr)):
    # 자연수 의 합 을 담아줄 변수 선언
    temp = 0
    # 시작값을 담아줌
    temp += arr[i]

    # 시작 값이 K와 같다면 경우의 수 +1
    if k == temp:
        cnt += 1

    # 시작값 다음 수 부터 하나씩 합하며 K와 같은 경우가 발생할 때마다 +1
    for j in range(i + 1, len(arr)):
        temp += arr[j]

        if k == temp:
            cnt += 1

print(cnt)