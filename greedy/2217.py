#로프
n = int(input())
arr = []
result = 0

for _ in range(n):
  arr.append(int(input()))

result = min(arr)
print(result * n)