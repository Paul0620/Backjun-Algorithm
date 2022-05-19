# 그리디 유형, 모험가 길드

import re
from unittest import result


n = 5
t = [2, 3, 1, 2, 2]
t.sort()  # 오름차순으로 정렬

result = 0
cnt = 0  # 모험가 수를 세기위한 카운트

for i in t:
    cnt += 1  # 현재 그룹에 모험가 포함시키기
    if cnt >= i:  # 모험가 수가 공포도보다 크거나 같다면
        result += 1  # 총 그룹 수 증가
        cnt = 0  # 모험가 수 초기화

print(result)
