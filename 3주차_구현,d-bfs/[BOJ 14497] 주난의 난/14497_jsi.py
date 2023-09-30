# 0-1 bfs 
# 0인 곳 다 돌고 0과 인접한 부분을 돎
# visited를 기록하므로 새롭게 0이 된 부분도 다 돌고

from collections import deque

N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[-1] * M for _ in range(N)]
map = []

for _ in range(N):
    map.append(list(input()))

def bfs(start_x, start_y):
    q = deque([(start_x, start_y)])
    visited[start_x][start_y] = 0

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                if map[nx][ny] == '0':
                    q.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                elif map[nx][ny] == '1' or map[nx][ny] == '#':
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
bfs(x1-1, y1-1)
print(visited[x2-1][y2-1])