'''
[ 0-1 bfs 기억해두기 ]
1. 0,1 두가지 가중치가 존재하는 bfs 문제 -> 가중치가 0인 경우와 1인 경우를 구분한다.
2. 가중치 0 인 경우가 더 좋은 탐색경로이므로, 큐에 넣을때 appendleft 를 통해 왼쪽에 넣는다.
'''

from collections import deque

m,n = map(int,input().split())
_map = []
for _ in range(n):
    _map.append(list(map(int,input())))

visited = [[-1]*m for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(start_x,start_y):
    q = deque([(start_x,start_y)])
    visited[start_x][start_y] = 0
    
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]

            if not 0<=nx<n or not 0<=ny<m: continue

            if visited[nx][ny] == -1:
                if _map[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y]
                    q.appendleft((nx,ny))
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
           
bfs(0,0)

print(visited[n-1][m-1])