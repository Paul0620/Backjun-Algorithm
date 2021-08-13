# 로프
n = int(input())
ropes = []
result = []

# 로프 무게 배열로 담기
for _ in range(n):
    ropes.append(int(input()))

# 내림차순으로 정렬
ropes.sort(reverse=True)

# 각 해당로프의 무게를 감당할 수 있는 로프 갯수를 곱하여 결과배열에 담기
for j in range(n):
    result.append(ropes[j] * (j+1))

# 계산하여 담은 값중 제일 높은 값 출력
print(max(result))
