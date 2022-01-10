temp = []

for _ in range(10):
    n = int(input())
    n %= 42
    temp.append(n)

# len의 시간복잡도 O(1), set의 시간복잡도 O(1)
print(len(set(temp)))
