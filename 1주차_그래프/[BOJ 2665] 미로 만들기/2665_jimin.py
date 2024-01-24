'''
1. 검은 방을 최대한 적게 지나간다. -> 흰 방이 우선순위를 갖는다. -> 0-1 bfs 사용
'''
from collections import deque

n = int(input())
_map = []
for _ in range(n):
    _map.append(list(input()))

visited = [[-1] * n for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(start_x,start_y):
    q = deque([(start_x,start_y)])
    visited[start_x][start_y] = 0

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=n: continue

            if nx==n-1 and ny==n-1:
                print(visited[x][y])
                exit()

            if _map[nx][ny] == '1':
                if visited[nx][ny] == -1:
                    q.appendleft((nx,ny))
                    visited[nx][ny] = visited[x][y]
            else:
                if visited[nx][ny] == -1:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1

bfs(0,0)