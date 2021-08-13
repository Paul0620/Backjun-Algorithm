# 회의실 배정
import sys

n = int(sys.stdin.readline())  # 드링크 수
times = [list(map(int, sys.stdin.readline().split()))
         for _ in range(n)]  # 시작 시간, 끝나는 시간을 배열로 받음
cnt = temp = 0
# 끝나는 시간을 기준으로 오름차순 정렬 후 시작 시간을 기준으로 오름차순 정렬
times.sort(key=lambda x: (x[1], x[0]))
print(times)

for time in times:
    if time[0] >= temp:  # 시작시간이 temp(끝나는 시간)보다 크거나 같다면
        temp = time[1]  # 끝나는 시간을 temp에 담음
        cnt += 1  # 회의실 가능 수 1 증가

print(cnt)
