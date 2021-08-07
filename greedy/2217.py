#로프
n = int(input())
arr = []
result = 0

for _ in range(n):
  arr.append(int(input()))

result = min(arr)
print(result * n)


"""
#로프
n = int(input())

ropes = []
result = []

for _ in range(n):
  ropes.append(int(input()))
ropes.sort(reverse=True)

for j in range(n):
  result.append(ropes[j] * (j + 1))

print(max(result))
"""