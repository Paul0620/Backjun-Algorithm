from itertools import combinations

n, m = map(int, input().split())

card_list = list(map(int, input().split()))
com_list = list(combinations(card_list, 3))
sum_list = []

for i in com_list:
    sum_list.append(sum(i))

if m in sum_list:
    print(m)
else:
    sum_list = sorted(set(sum_list))
    print(sum_list)
    temp = []

    for i in sum_list:
        if i > m:
            temp.append(i - m)
        else:
            temp.append(m - i)

    print(sum_list[temp.index(min(temp))])
