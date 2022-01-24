n = int(input())
nums = 1
answer = 1

while n > nums:
    nums += 6 * answer
    answer += 1

print(answer)
