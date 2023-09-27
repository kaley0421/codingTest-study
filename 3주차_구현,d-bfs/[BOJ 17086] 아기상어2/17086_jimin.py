from collections import deque

n,m = map(int,input().split())
_map = []
for _ in range(n):
    _map.append(list(map(int,input().split())))

visited = [[-1]*m for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if _map[i][j] == 1: 
            q.append((i,j))
            visited[i][j] = 0

dx = [-1,0,1,0,-1,-1,1,1]
dy = [0,-1,0,1,-1,1,-1,1]

def bfs():
    while q:
        x,y = q.popleft()
        cur_step = visited[x][y]

        for i in range(8):
            nx,ny = x+dx[i], y+dy[i]
            
            if not 0<=nx<n or not 0<=ny<m: continue

            if visited[nx][ny] == -1:
                visited[nx][ny] = cur_step + 1
                q.append((nx,ny))
            elif visited[nx][ny] > cur_step + 1:
                visited[nx][ny] = cur_step + 1
                q.append((nx,ny))

bfs()

answer = 0
for i in range(n):
    for j in range(m):
        answer = max(answer,visited[i][j])
print(answer)