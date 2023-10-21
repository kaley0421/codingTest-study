''' 1트
[ 틀린 이유 ]
1. 3번 테케에서 첫번째 죄수가 나가기 위해 열어야 하는 문의 최소 개수 => 5, 두번째 죄수가 열어야 하는 문 => 5 라서 답이 10으로 나옴.
    : 첫번째 죄수가 6개의 문을 열고 나가고, 두번째 죄수가 3개의 문을 열고 나가면 총 9개로 나갈 수 있으므로, 이 경우를 고려해야.
'''
# from collections import deque

# t = int(input())

# def bfs(start_x,start_y):
#     global answer, opening_doors, end_x, end_y

#     q = deque([(start_x,start_y)])
#     visited[start_x][start_y] = 0
#     _map[start_x][start_y] = '.'
#     opening_doors[(start_x,start_y)] = []

#     while q:
#         x,y = q.popleft()

#         if x==0 or x==h-1 or y==0 or y==w-1:
#             answer += visited[x][y]
#             end_x, end_y = x,y
#             break

#         for i in range(4):
#             nx, ny = x+dx[i], y+dy[i]

#             if not 0<=nx<h or not 0<=ny<w: continue

#             if visited[nx][ny] == -1 and _map[nx][ny] != '*':
#                 if _map[nx][ny] == '.' or _map[nx][ny] == '$':         # 빈 공간
#                     q.appendleft((nx,ny))
#                     visited[nx][ny] = visited[x][y]
#                     opening_doors[(nx,ny)] = opening_doors[(x,y)]
#                 elif _map[nx][ny] == '#':       # 문 열기
#                     q.append((nx,ny))
#                     visited[nx][ny] = visited[x][y] + 1
#                     opening_doors[(nx,ny)] = opening_doors[(x,y)] + [(nx,ny)]
#     return end_x, end_y
                
# dx = [-1,0,1,0]
# dy = [0,-1,0,1]
# answer = 0
# opening_doors = dict()
# end_x,end_y = 0,0

# for _ in range(t):
#     _h,_w = map(int,input().split())
#     h,w = _h+2, _w+2
#     _map = []
#     _map.append(['.']*(w))
#     for _ in range(_h):
#         _map.append(['.']+list(input())+['.'])
#     _map.append(['.']*(w))

#     visited = [[-1]*(w) for _ in range(h)]
#     answer = 0
    
#     prisoners = []
#     for i in range(h):
#         for j in range(w):
#             if _map[i][j] == '$':
#                 prisoners.append((i,j))
    
#     for px,py in prisoners:
#         opening_doors = dict()
#         visited = [[-1]*(w) for _ in range(h)]
#         end_x, end_y = bfs(px,py)
#         # open doors
#         for door_x, door_y in opening_doors[(end_x,end_y)]:
#             _map[door_x][door_y] = '.'

#     print("--- ans: ", answer)
   


''' 2트 => 10 % 에서 틀림.
1. _map 의 가장자리에 총 몇 개의 문을 열고 나왔는지 저장하므로, 
    첫번째 죄수에 대해 bfs 실행 -> 두번째 죄수에 대해 bfs 실행 -> _map 가장자리에서 최솟값 찾기
    : 각 죄수별로 visited 배열 2개 사용
2. visited[x][y] = n
    : (x,y) 까지 도달하기 위해 연 문의 개수
3. opening_doors[(x,y)] = []
    : (x,y) 까지 도달하기 위해 연 문의 position list
    : 첫번째 죄수의 opening_doors 와 두번째 죄수의 opening_doors 에 겹치는 게 있다면, 마지막에 개수 셀 때 빼준다.

[ 반례 ]
1
6 7
****#**
*##..**
*.**.**
*$###**
***$***
*******
답: 4 / 내 답: 5
=> 첫번째 죄수 기준 (1,5) 에 도달하려면 (2,2),(2,3),(1,5) 를 열고 가는게 최적이지만,
    두번째 죄수까지 고려했을 때 (4,3),(4,4),(4,5) 로 가는게 더 좋은 방법임.
=> 어떻게 고려해..?..
'''
from collections import deque

t = int(input())

def bfs(start_x,start_y,p_idx): 
    global opening_doors

    q = deque([(start_x,start_y)])
    visited[p_idx][start_x][start_y] = 0
    _map[start_x][start_y] = '.'
    opening_doors[p_idx][(start_x,start_y)] = []
    
    while q:
        x,y = q.popleft()

        if x==0 or x==h-1 or y==0 or y==w-1:
            continue
        else:
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]

                if not 0<=nx<h or not 0<=ny<w: continue

                if visited[p_idx][nx][ny] == -1 and _map[nx][ny] != '*':
                    if _map[nx][ny] == '.' or _map[nx][ny] == '$':                      # 빈 공간
                        q.appendleft((nx,ny))
                        visited[p_idx][nx][ny] = visited[p_idx][x][y]
                        opening_doors[p_idx][(nx,ny)] = opening_doors[p_idx][(x,y)]
                    elif _map[nx][ny] == '#':                                           # 문 열기
                        q.append((nx,ny))
                        visited[p_idx][nx][ny] = visited[p_idx][x][y] + 1
                        opening_doors[p_idx][(nx,ny)] = opening_doors[p_idx][(x,y)] + [(nx,ny)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

for _ in range(t):
    _h,_w = map(int,input().split())
    h,w = _h+2, _w+2
    _map = []
    _map.append(['.']*(w))
    for _ in range(_h):
        _map.append(['.']+list(input())+['.'])
    _map.append(['.']*(w))

    visited = [[[-1]*(w) for _ in range(h)] for _ in range(2)]
    opening_doors = [dict() for _ in range(2)]
    prisoners = []
    for i in range(h):
        for j in range(w):
            if _map[i][j] == '$':
                prisoners.append((i,j))
    
    for i in range(2):
        bfs(prisoners[i][0],prisoners[i][1],i)
    
    # # visited 배열 출력
    # for idx in range(2):
    #     print("--- visited ", idx)
    #     for i in range(h):
    #         for j in range(w):
    #             print(visited[idx][i][j], end = " ")
    #         print()
        
    # _map 가장자리의 visited 값 확인
    answer = 1e9
    for i in [0,h-1]:
        for j in range(w):
            cnt = visited[0][i][j] + visited[1][i][j]
            if (i,j) in opening_doors[0].keys() and (i,j) in opening_doors[1].keys():
                for x,y in opening_doors[0][(i,j)]:
                    if (x,y) in opening_doors[1][(i,j)]:
                        cnt -= 1
            if cnt >= 0: answer = min(answer, cnt)
    for i in range(h):
        for j in [0,w-1]:
            cnt = visited[0][i][j] + visited[1][i][j]
            if (i,j) in opening_doors[0].keys() and (i,j) in opening_doors[1].keys():
                for x,y in opening_doors[0][(i,j)]:
                    if (x,y) in opening_doors[1][(i,j)]:
                        cnt -= 1
            if cnt >= 0: answer = min(answer, cnt)
   
    print(answer)