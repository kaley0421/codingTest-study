'''
1. spread 함수 틀린 이유 ?_?
    : map 값을 바로바로 업데이트 하면 데이터 불일치 문제 발생 -> diffused 배열을 필터처럼 만들어서, 확산 변경사항을 한번에 반영해준다.

2. dx, dy, direction 을 설정해서 시계/반시계 방향 회전 구현하는 법 기억해둘것
'''
import sys

r,c,t = map(int,input().split())
_map = []
for _ in range(r):
    _map.append(list(map(int,sys.stdin.readline().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

# def spread(pos_list):
#     global r,c

#     for x,y in pos_list:
#         spread_amount = _map[x][y] // 5
#         spread_cnt = 0

#         for i in range(4):
#             nx,ny = x+dx[i], y+dy[i]
            
#             if nx<0 or nx>=r or ny<0 or ny>=c: continue
#             if _map[nx][ny] == -1: continue

#             _map[nx][ny] += spread_amount
#             spread_cnt += 1
        
#         _map[x][y] -= spread_amount * spread_cnt

def diffuse():
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
    diffused = [[0] * c for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if _map[x][y] == 0 or _map[x][y] == -1:
                continue

            dust = _map[x][y] // 5

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < r and 0 <= ny < c and _map[nx][ny] != -1:
                    diffused[nx][ny] += dust
                    diffused[x][y] -= dust

    for i in range(r):
        for j in range(c):
            _map[i][j] += diffused[i][j]


def rotate_top(machine):
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]

    x,y,direct = machine[0],1,0
    prev = 0
    
    while True:
        nx,ny = x+dx[direct], y+dy[direct]
        
        if x == machine[0] and y == 0: break
        if not 0<=nx<r or not 0<=ny<c: 
            direct += 1
            continue
        
        _map[x][y], prev = prev, _map[x][y]
        x,y = nx,ny


def rotate_bottom(machine):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    x,y,direct = machine[1],1,0
    prev = 0

    while True:
        nx,ny = x+dx[direct], y+dy[direct]

        if x == machine[1] and y == 0: break
        if not 0<=nx<r or not 0<=ny<c: 
            direct += 1
            continue
        
        _map[x][y], prev = prev, _map[x][y]
        x,y = nx,ny


for _ in range(t):
    machine = []
    pos_list = []
    for i in range(r):
        for j in range(c):
            if _map[i][j]>0: pos_list.append((i,j))
            if _map[i][j]==-1: machine.append(i)

    #spread(pos_list)
    diffuse()

    rotate_top(machine)
    rotate_bottom(machine)

answer = 2
for i in range(r):
    for j in range(c):
        answer += _map[i][j]
print(answer)