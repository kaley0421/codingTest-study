from itertools import combinations
from collections import deque

N, M = map(int, input().split())
MAP = []
virus, wall = [], []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(N):
    MAP.append(list(map(int, input().split())))
    for j in range(N):
        if MAP[-1][j] == 2:
            virus.append((i, j))
        elif MAP[-1][j] == 1:
            wall.append((i, j))

def bfs(_map, q):
    time = 0

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                if _map[nx][ny] == -1:
                    _map[nx][ny] = _map[x][y] + 1
                    q.append((nx, ny))
                    time = max(time, _map[nx][ny])
                elif _map[nx][ny] == -3:
                    _map[nx][ny] = _map[x][y] + 1
                    q.append((nx, ny))
    return time

answer = 1e9

for _list_active_virus in combinations(virus, M):
    MAP_time = [[-1] * N for _ in range(N)]
    q = deque([])

    for wall_x, wall_y in wall:
        MAP_time[wall_x][wall_y] = -2
    
    for virus_x, virus_y in virus:
        MAP_time[virus_x][virus_y] = -3
    
    for active_virus_x, active_virus_y in _list_active_virus:
        MAP_time[active_virus_x][active_virus_y] = 0
        q.append((active_virus_x, active_virus_y))
        
    time = bfs(MAP_time, q)
    if time < answer:
        is_all_spread = True
        
        for i in range(N):
            if MAP_time[i].count(-1) > 0:
                is_all_spread = False
                break
        
        if is_all_spread:
            answer = time

print(answer) if answer < 1e9 else print(-1)