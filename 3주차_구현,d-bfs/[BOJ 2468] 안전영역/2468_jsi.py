import sys
from collections import deque

N = int(input())
_map = []

for i in range(N):
    _map.append(list(map(int, sys.stdin.readline().split())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
_min, _max = min([min(i) for i in _map]), max([max(i) for i in _map])
result = 0

def bfs(start_x, start_y, visited, len_rain):
    q = deque([(start_x, start_y)])
    
    visited[start_x][start_y] = True

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and _map[nx][ny] > len_rain:
                visited[nx][ny] = True
                q.append((nx, ny))

for len_rain in range(_min, _max + 1):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if _map[i][j] > len_rain and not visited[i][j]:
                bfs(i, j, visited, len_rain)
                cnt += 1
    result = max(result, cnt)

print(result if result != 0 else 1)