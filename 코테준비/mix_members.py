import random, math, datetime

start = datetime.datetime.now() 

# 임의의 멤버 수 정하기
member_cnt = random.randint(10, 100)
# 전체 멤버를 담을 리스트
members = []
# 랜덤한 조를 담을 딕셔너리
group = {}
# 조의 개수를 최소화 하기 위해 한 조의 최대 인원수인 7로 전체 멤버 수를 나누어 반올림으로 조의 개수를 구한다.
group_cnt = math.ceil(member_cnt / 7)

# 중복되지 않은 이름(숫자를 문자형으로 변환)을 멤버 수 만큼 담기
while True:
    m = random.randint(1, member_cnt)
    if m not in members:
        members.append(m)

    if member_cnt == len(members):
        break

# members 리스트에서 랜덤하게 한 명씩 빼내어 1조부터 n조까지 한 명씩 담는다.
while True:
    for cnt in range(1, group_cnt + 1):
        r = members.pop(members.index(random.choice(members)))

        if f'{cnt}조' not in group:
            group[f'{cnt}조'] = [r]
        else:
            group[f'{cnt}조'] += [r]    
    
        if len(members) == 0:
            break
    
    if len(members) == 0:
        break


end = datetime.datetime.now() 

print(f'멤버 수 : {member_cnt}, 조의 개수 : {group_cnt}')
print(group)

time = end - start

print(f'time : {time.microseconds}')