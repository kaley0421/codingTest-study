# 다시 풀어보면 좋을 bfs
# 한 번에 거리가 1이 아닐 수 있음 !!
# 재방문이 가능하다면
# visited[nx][ny] == 0 or visited[nx][ny] == visited[x][y] + 1
# 거칠 수 있다면
# visited[nx][ny] == visited[x][y] + 1은 q에 넣지 않음
# 45라인 넣어서 시간초과 사라졌다 -> 필요 없는 거 break 걸어서 없애기

import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[-1] * M for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(N):
    _list = list(input())
    for j in range(M):
        if _list[j] == '.':
            graph[i][j] = 0

def bfs(start_x, start_y, end_x, end_y):
    q = deque([(start_x, start_y)])
    graph[start_x][start_y] = 0

    while q:
        x, y = q.popleft()

        if x == end_x and y == end_y:
            return graph[x][y]
            
        for k in range(4):
            for t in range(1, K + 1):
                nx, ny = x + dx[k] * t, y + dy[k] * t

                if nx < 0 or N <= nx or ny < 0 or M <= ny or graph[nx][ny] == -1:
                    break
                if graph[nx][ny] == 0:
                    q.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1
                elif graph[nx][ny] == graph[x][y] + 1:
                    continue
                else:
                    break
    return -1

x1, y1, x2, y2 = map(int, input().split())

print(bfs(x1-1, y1-1, x2-1, y2-1))


"""
1. 96%에서 시간 초과 -> 중복 조건을 제거함
import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[False] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(N):
    _list = list(input().rstrip())
    for j in range(M):
        if _list[j] == '.':
            graph[i][j] = True

def bfs(start_x, start_y, end_x, end_y):
    q = deque([(start_x, start_y, 0)])
    visited[start_x][start_y] = 1

    while q:
        x, y, time = q.popleft()

        if (x, y) == (end_x, end_y):
            return time
            
        for k in range(4):
            for t in range(1, K + 1):
                nx, ny = x + dx[k] * t, y + dy[k] * t

                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny]:
                    if visited[nx][ny] == 0:
                        q.append((nx, ny, time + 1))
                        visited[nx][ny] = 1
                else:
                    break
    return -1

x1, y1, x2, y2 = map(int, input().split())

print(bfs(x1-1, y1-1, x2-1, y2-1))
"""