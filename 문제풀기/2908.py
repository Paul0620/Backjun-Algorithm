from audioop import reverse


a, b = input().split()


def fn_reverse(num):
    num_reverse = ""

    for i in num:
        num_reverse = i + num_reverse

    return int(num_reverse)


max(fn_reverse(a), fn_reverse(b))
