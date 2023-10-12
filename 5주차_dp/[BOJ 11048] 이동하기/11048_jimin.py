from collections import deque

def bfs(start_x,start_y):
    q = deque([(start_x,start_y)])
    visited[start_x][start_y] = _map[start_x][start_y]

    while q:
        x,y = q.popleft()
        
        for i in range(3):
            nx,ny = x+dx[i], y+dy[i]

            if not 0<=nx<n or not 0<=ny<m: continue

            if visited[nx][ny] < visited[x][y] + _map[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + _map[nx][ny]
        
n,m = map(int,input().split())
_map = []
for _ in range(n):
    _map.append(list(map(int,input().split())))

dx = [0,1,1]
dy = [1,0,1]
visited = [[-1]*m for _ in range(n)]

bfs(0,0)

print(visited[n-1][m-1])