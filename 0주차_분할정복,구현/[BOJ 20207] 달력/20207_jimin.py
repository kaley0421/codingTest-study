''' 1트 => 왜 틀렸는지 모르겠..
1. map 초기화 잘못된듯
'''
# n = int(input())
# schedules = []
# max_e = 0
# for _ in range(n):
#     s,e = map(int,input().split())
#     max_e = max(max_e,e)
#     schedules.append((s,e))
# min_s = schedules[0][0]

# schedules.sort(key = lambda x : (x[0], -(x[1]-x[0])))

# _map = [[-1]*(max_e-min_s+1) for _ in range(n)]

# def check_avail(i,start_idx,end_idx):
#     for j in range(start_idx, end_idx+1):
#         if _map[i][j] != -1: return False
#     return True

# for (s,e) in schedules:
#     start_idx, end_idx = s-min_s, e-min_s
#     for i in range(n):
#         if _map[i][start_idx] == -1 and check_avail(i,start_idx,end_idx) == True:
#             for j in range(start_idx, end_idx+1):
#                 _map[i][j] = 0
#             break

# def check_is_sch(day):
#     for j in range(n):
#         if _map[j][day] == 0:
#             return True
#     return False

# def get_height(day):
#     min_y, max_y = 1e9, 0
#     for j in range(n):
#         if _map[j][day] == 0:
#             min_y = min(min_y,j)
#             max_y = max(max_y,j)
#     return (min_y, max_y)

# visited = [False]*(max_e-min_s+1)
# def process(day):
#     if visited[day]: return 0
#     if check_is_sch(day) == False: return 0
    
#     min_x, max_x = day, day
#     min_y, max_y = get_height(day)
#     visited[day] = True

#     while True:
#         day += 1
#         if day >= max_e-min_s+1: break
#         visited[day] = True
#         if not check_is_sch(day): break

#         max_x = day
#         mi_y, ma_y = get_height(day)
#         min_y, max_y = min(min_y, mi_y), max(max_y,ma_y)
#     return (max_y-min_y+1)*(max_x-min_x+1)

# answer = 0
# for i in range(max_e-min_s+1):
#     answer += process(i)

# print(answer)

''' 2트 => 답 참고
'''
n = int(input())

_map = [[-1] * 366 for _ in range(n)]
schedules = list()
for _ in range(n):
    s, e = map(int, input().split(' '))
    term = e - s + 1
    schedules.append((s, e, term))

schedules.sort(key=lambda x: (x[0], -x[2]))

for k in range(len(schedules)):
    s, e = schedules[k][0], schedules[k][1]

    for i in range(n):
        if 0 in _map[i][s:e + 1]:
            continue

        for j in range(s, e + 1):
            _map[i][j] = 0
        break

row, col = 0,0
answer = 0
for day in range(1,366):
    is_sch = False
    for i in range(n):
        if _map[i][day] == 0:
            is_sch = True
            row = max(row, i+1)
    if is_sch:
        col += 1
    else:
        answer += row * col
        row, col = 0, 0
if is_sch:
    answer += row * col

print(answer)