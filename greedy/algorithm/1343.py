# 폴리오미노
n = input()  # 입력값 받음

# XXXX가 4개는 AAAA로 XX가 두개는 BB로 replace로 치환
n = n.replace('XXXX', 'AAAA')
n = n.replace('XX', 'BB')

# 치환한뒤에 X가 있다면 -1 출력
if 'X' in n:
    print(-1)
# 아니면 치환된거 출력
else:
    print(n)
