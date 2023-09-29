# bfs로 되는지

import sys
from collections import deque

M, N = map(int, input().split())
graph = []
visited = [[-1] * M for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

def bfs(start_x, start_y):
    q = deque([(start_x, start_y)])
    visited[start_x][start_y] = 0

    while q:
        x, y = q.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y]

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    q.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    return -1

print(bfs(0, 0))