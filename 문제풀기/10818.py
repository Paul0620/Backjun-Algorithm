n = int(input())
m = list(map(int, input().split()))

# max, min의 시간 복잡도 O(n)
print(min(m), max(m))
