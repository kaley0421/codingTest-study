# N * M개 영역 탐색 -> 살아남은 빙산 glacier 탐색으로 바꿈

import sys
from collections import deque

N, M = map(int, input().split())
_map = []
glacier = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(N):
    _map.append(list(map(int, sys.stdin.readline().split())))

    for j in range(M):
        if _map[i][j] != 0:
            glacier.append([i, j, _map[i][j]])

def bfs(start_x, start_y):
    q = deque([(start_x, start_y)])
    visited[start_x][start_y] = True

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and _map[nx][ny] > 0:
                q.append((nx, ny))
                visited[nx][ny] = True

def melt():
    _map_melted = []
    glacier.clear()

    for i in range(N):
        for j in range(M):
            if _map[i][j] == 0:
                continue
            
            cnt = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]

                if 0 <= nx < N and 0 <= ny < M and _map[nx][ny] == 0:
                    cnt += 1

            _map_melted.append([i, j, cnt])
    
    while _map_melted:
        x, y, cnt = _map_melted.pop()

        if _map[x][y] != 0:
            _map[x][y] -= min(cnt, _map[x][y])
        if _map[x][y] != 0:
            glacier.append([x, y,_map[x][y]])

cnts = []
while True:
    visited = [[False] * M for _ in range(N)]
    num_glacier = len(glacier)
    cnt = 0

    for i in range(num_glacier):
        x, y, k = glacier[i]

        if not visited[x][y]:
            bfs(x, y)
            cnt += 1
    cnts.append(cnt)

    if cnt == 0 and len(cnts) > 0:
        print(0)
        break
    elif cnt >= 2:
        print(len(cnts) - 1)
        break

    melt()

"""
import sys
from collections import deque

N, M = map(int, input().split())
_map = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(N):
    _map.append(list(map(int, sys.stdin.readline().split())))

def bfs(start_x, start_y):
    q = deque([(start_x, start_y)])
    visited[start_x][start_y] = True

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and _map[nx][ny] > 0:
                q.append((nx, ny))
                visited[nx][ny] = True

def melt():
    _map_melted = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if _map[i][j] == 0:
                continue
            
            cnt = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]

                if 0 <= nx < N and 0 <= ny < M and _map[nx][ny] == 0:
                    cnt += 1

            _map_melted[i][j] = cnt
    
    for i in range(N):  
        for j in range(M):
            if _map[i][j] != 0:
                _map[i][j] -= min(_map_melted[i][j], _map[i][j])

result = 0

while True:
    cnt = 0
    visited = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if _map[i][j] > 0 and not visited[i][j]:
                bfs(i, j)
                cnt += 1

    if cnt >= 2 or (cnt == 0 and result > 0):
        print(result)
        break

    melt()
    result += 1
"""