from datetime import datetime
from collections import deque

def make_timetable(a_time, b_time, c_time, d_time):
    # 시간표
    answer = [[0 for _ in range(8)] for _ in range(5)]
    # 알바 시간표를 리스트에 다 담기
    part_list = [a_time, b_time, c_time, d_time]
    # 딕셔너리에 담기위한 키명들
    p_list = ['A', 'B', 'C', 'D']
    # 근로시간 카운트
    p_cnt = [0 for _ in range(len(p_list))]


    # 각 요일별로 파트타이머들의 근무 가능 시간 가져오기
    for i in range(5):
        # 해당 요일에 시간순으로 정리하기 위한 리스트 생성
        time_table = []
        
        for j in range(len(part_list)):
            for k in part_list[j][i].split(';'):
                temp = []
                for h in k.split('~'):
                    temp += [int(h.replace(':00', ''))]
                time_table.append([p_list[j], temp])

        # 시간이 빠른순으로 정렬
        time_table.sort(key=lambda x : x[1])

        # 빠른순으로 꺼내기 위해 deque사용
        que = deque(time_table)

        for i in range(len(time_table)):
            part = time_table[i][0]
            time = time_table[i][1]

        print(time_table)

            


a_time = ['10:00~14:00', '15:00~18:00', '11:00~13:00;14:00~16:00', '10:00~11:00', '15:00~18:00']
b_time = ['11:00~14:00', '14:00~16:00', '16:00~18:00', '10:00~11:00;12:00~13:00', '14:00~16:00']
c_time = ['14:00~16:00', '16:00~18:00', '10:00~12:00', '12:00~14:00', '14:00~16:00']
d_time = ['14:00~18:00', '10:00~18:00', '12:00~14:00', '14:00~15:00;16:00~17:00', '10:00~12:00']

make_timetable(a_time, b_time, c_time, d_time)

