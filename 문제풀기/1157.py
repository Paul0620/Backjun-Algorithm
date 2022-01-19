n = input()
check = []


for i in list(n.lower()):
    if i not in check:
        check[i] += 1
    print(check)
