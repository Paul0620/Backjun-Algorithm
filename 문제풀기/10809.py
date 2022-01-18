from string import ascii_lowercase

n = input()
alphaber = list(ascii_lowercase) # 알파벳 소문자 리스트형으로 
answer = [] # 결과값 리스트
check = [] # 체크한 알파벳을 담아두기 위한 리스트

for i in alphaber:
    if i in n:
        if i not in check:
            answer.append(n.index(i))
    else:
        answer.append(-1)

for j in answer:
    print(j, end=' ')