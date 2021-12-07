# 2941 크로아티아 알파벳 실버5

c_string = input()

c_string = c_string.replace("c=", "0")
c_string = c_string.replace("c-", "0")
c_string = c_string.replace("dz=", "0")
c_string = c_string.replace("d-", "0")
c_string = c_string.replace("lj", "0")
c_string = c_string.replace("nj", "0")
c_string = c_string.replace("s=", "0")
c_string = c_string.replace("z=", "0")

answer = len(c_string)

print(answer)
