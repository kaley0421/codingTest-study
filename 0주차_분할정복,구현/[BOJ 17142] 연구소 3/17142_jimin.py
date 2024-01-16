from itertools import combinations
from collections import deque

n,m = map(int,input().split())
_map = []
for _ in range(n):
    _map.append(list(map(int,input().split())))

# 활성 바이러스 고르기
candis = []
for i in range(n):
    for j in range(n):
        if _map[i][j] == 2:
            candis.append((i,j))
virus = list(combinations(candis,m))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def spread(visited, virus):
    q = deque()
    for i in range(len(virus)):
        q.append(virus[i])
        visited[virus[i][0]][virus[i][1]] = 0
    
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n: continue
            # 벽일 경우
            if _map[nx][ny] == 1: continue
            # 바이러스일 경우
            if _map[nx][ny] == 2 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
            # 빈칸일 경우
            if _map[nx][ny] == 0 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))

def cnt(visited):
    time = 0
    for i in range(n):
        for j in range(n):
            if _map[i][j] == 0:
                time = max(time, visited[i][j])
    return time

def verify(visited):
    for i in range(n):
        for j in range(n):
            if _map[i][j] == 0 and visited[i][j]<0: return False
    return True
            
answer = 1e9

for v in virus:
    temp = [[-1]*n for _ in range(n)]
    spread(temp,v)
    if verify(temp): 
        res = cnt(temp)
        answer = min(answer, res)

if answer == 1e9: print(-1)
else: print(answer)