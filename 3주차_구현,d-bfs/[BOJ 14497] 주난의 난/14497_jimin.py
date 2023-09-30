'''
[ 0-1 bfs ]
1. '최소' 값을 찾기 위해서 _map[nx][ny] == 0 인 경우 appendleft 가 필요
    : appendleft 안하고 그냥 append 로 하면 최소값을 못 찾는다..!
'''

from collections import deque

n,m = map(int,input().split())
x1,y1,x2,y2  = map(int,input().split())
_map = []
for _ in range(n):
    _map.append(list(input()))

visited = [[-1]*m for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(start_x,start_y):
    q = deque([(start_x,start_y)])
    visited[start_x][start_y] = 0

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if not 0<=nx<n or not 0<=ny<m: continue

            if visited[nx][ny] == -1:
                if _map[nx][ny] == '1' or _map[nx][ny] == "#":
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
                elif _map[nx][ny] == '0':
                    visited[nx][ny] = visited[x][y]
                    q.appendleft((nx,ny))
                
bfs(x1-1,y1-1)
print(visited[x2-1][y2-1]) 