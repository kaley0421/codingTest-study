from collections import deque

h,w = map(int,input().split())
blocks = list(map(int,input().split()))

_map = [[0]*w for _ in range(h)]
visited = [[0]*w for _ in range(h)]

for j in range(w):
    for i in range(blocks[j]):
        _map[i][j] = 1
        visited[i][j] = 1

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def check(x,y):
    global h,w

    if y == 0 or y == w-1: return False

    left_flag = False
    for j in range(y-1,-1,-1):
        if _map[x][j] == 1: left_flag = True
    
    right_flag = False
    for j in range(y+1,w):
        if _map[x][j] == 1: right_flag = True
    
    if right_flag == True and left_flag == True: return True
    return False

def bfs(start_x,start_y):
    global answer

    q = deque([(start_x,start_y)])
    visited[start_x][start_y] = 1
    
    if check(start_x,start_y) == True: answer += 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]

            if not 0<=nx<h or not 0<=ny<w: continue

            if visited[nx][ny] == 0:
                if check(nx,ny) == True: answer += 1
                q.append((nx,ny))
                visited[nx][ny] = True

answer = 0
for i in range(h):
    for j in range(w):
        if _map[i][j] == 0 and visited[i][j] == 0:
            bfs(i,j)
print(answer)