# 셀프 넘버 실버5

num = set(range(1, 10001))
rm_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    rm_num.add(i)

num = num - rm_num

for h in sorted(num):
    print(h)
