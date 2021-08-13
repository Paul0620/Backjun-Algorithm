# 거스름돈
n = int(input())
result = 0

while True:
    # 5의 배수라면 5로 나눠서 몫을 개수로 카운트
    if n % 5 == 0:
        result += n // 5
        print(result)
        break
    # 5의 배수가 아니라면 2씩 차감을 하고 카운트 +1
    n -= 2
    result += 1

    # 거스름돈 값이 0보다 작다면 -1 출력
    if n < 0:
        print(-1)
        break
