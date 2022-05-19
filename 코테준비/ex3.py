from unittest import result


# 그리디 유형문제, 곱하기 또는 더하기

s = "02984"

s1 = "567"

result = int(s[0])

for i in range(1, len(s)):
    num = int(s[i])
    # 두 수 중에서 하나라도 0이나 1이라면 더하기 수행
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
