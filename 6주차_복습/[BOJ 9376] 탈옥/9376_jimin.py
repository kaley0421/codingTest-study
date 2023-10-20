''' 1트 => 제 3자 고려가 안되는 듯.. 왜 틀렸는지 확인 필요.
'''
from collections import deque

t = int(input())

def bfs(start_x,start_y):
    global answer, opening_doors, end_x, end_y

    q = deque([(start_x,start_y)])
    visited[start_x][start_y] = 0
    _map[start_x][start_y] = '.'
    opening_doors[(start_x,start_y)] = []

    while q:
        x,y = q.popleft()

        if x==0 or x==h-1 or y==0 or y==w-1:
            answer += visited[x][y]
            end_x, end_y = x,y
            break

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if not 0<=nx<h or not 0<=ny<w: continue

            if visited[nx][ny] == -1 and _map[nx][ny] != '*':
                if _map[nx][ny] == '.' or _map[nx][ny] == '$':         # 빈 공간
                    q.appendleft((nx,ny))
                    visited[nx][ny] = visited[x][y]
                    opening_doors[(nx,ny)] = opening_doors[(x,y)]
                elif _map[nx][ny] == '#':       # 문 열기
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
                    opening_doors[(nx,ny)] = opening_doors[(x,y)] + [(nx,ny)]
    return end_x, end_y
                
dx = [-1,0,1,0]
dy = [0,-1,0,1]
answer = 0
opening_doors = dict()
end_x,end_y = 0,0

for _ in range(t):
    _h,_w = map(int,input().split())
    h,w = _h+2, _w+2
    _map = []
    _map.append(['.']*(w))
    for _ in range(_h):
        _map.append(['.']+list(input())+['.'])
    _map.append(['.']*(w))

    visited = [[-1]*(w) for _ in range(h)]
    answer = 0
    
    prisoners = []
    for i in range(h):
        for j in range(w):
            if _map[i][j] == '$':
                prisoners.append((i,j))
    
    for px,py in prisoners:
        opening_doors = dict()
        visited = [[-1]*(w) for _ in range(h)]
        end_x, end_y = bfs(px,py)
        # open doors
        for door_x, door_y in opening_doors[(end_x,end_y)]:
            _map[door_x][door_y] = '.'

    print("--- ans: ", answer)
   