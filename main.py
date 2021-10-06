a = [[60, 50], [30, 70], [60, 30], [80, 40]]
b = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
c = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

# 1. w, h중 한쪽은 최대값을 사용
# 2. 나머지 하나 값에서 회전시켰을 때 그 값보다 큰지
# 3. 크다면 그 중 가장 최소값을 찾아야함.

def solution(sizes):
    answer = 0
    w = 0
    h = 0
    for i in sizes:
        i.sort()
        if w < i[0]:
            w = i[0]
        if h < i[1]:
            h = i[1]

    answer = w * h

    return answer


print(solution(a))
print(solution(b))
print(solution(c))