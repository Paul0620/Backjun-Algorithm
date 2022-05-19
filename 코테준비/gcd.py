def gcd(a, b):
    if a % b == 0:  # a를 b로 나눈 나머지가 0이라면
        return b
    else:
        return gcd(b, a % b)  # 재귀 함수를 통해 한번더 계산


print(gcd(192, 162))
