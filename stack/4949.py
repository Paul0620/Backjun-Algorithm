# 4949 균형잡힌 세상 실4
while True:
    n = input().rstrip()
    s_list = []
    check = 0

    if n == ".":
        break

    for i in n:
        if i == "(" or i == "[":
            s_list.append(i)
        elif i == ")":
            if not s_list or s_list[-1] == "[":
                print("no")
                check = 1
                break
            else:
                s_list.pop()
        elif i == "]":
            if not s_list or s_list[-1] == "(":
                print("no")
                check = 1
                break
            else:
                s_list.pop()

    if check == 0:
        if not s_list:
            print("yes")
        else:
            print("no")
