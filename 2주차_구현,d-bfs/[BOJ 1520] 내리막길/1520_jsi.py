# dfs(x, y)와 DP[x][y]의 의미를 명시하자!
# dfs(x, y) = (x, y)에서 도착지점까지 가는 방법 수
# DP[x][y] = (x, y)에서 도착지점까지 가는 방법 수
# DP[nx][ny] = 전 단계들의 가짓수 합

# bfs + heap + DP로 못 하나?
# 간 적이 있는데 길이 없는 걸 수도?
import sys

input = sys.stdin.readline

M, N = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
DP = [[-1] * N for _ in range(M)]
L = []

for _ in range(M):
    L.append(list(map(int, input().split())))

def dfs(x, y):
    if x == M-1 and y == N-1:
        return 1
    
    if DP[x][y] != -1:
        return DP[x][y]

    cnt = 0
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < M and 0 <= ny < N and L[nx][ny] < L[x][y]:
            cnt += dfs(nx, ny)
        
    DP[x][y] = cnt
    
    return DP[x][y]

print(dfs(0, 0))

"""import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
L = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
DP = [[] * N for _ in range]
for _ in range(M):
    L.append(list(map(int, input().split())))

def bfs(start_x, start_y):
    q = deque()
    q.append((start_x, start_y, 0))
    
    DP[start_x][start_y] = 1

    answer = 0

    while q:
        x, y, dist = q.popleft()
        if x == M - 1 and y == N - 1:
            answer += 1
            continue
        
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            
            if 0 <= nx < M and 0 <= ny < N and L[nx][ny] < L[x][y]:
                DP[nx][ny] += 1
                q.append((nx, ny, dist + 1))
    return answer

print(bfs(0, 0))
"""