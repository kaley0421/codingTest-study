import copy
import sys

input = sys.stdin.readline

R, C, T = map(int, input().split())
A, dust = [], []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
purifier = []

for i in range(R):
    A.append(list(map(int, input().split())))
    for j in range(C):
        if A[i][j] == -1:
            purifier.append((i, j))

def defuse(x, y, graph):
    cnt = 0
    if (x, y) in purifier or graph[x][y] == 0:
        return

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
            dust[nx][ny] += graph[x][y] // 5
            cnt += 1
    
    dust[x][y] += graph[x][y] - (graph[x][y] // 5) * cnt

def purify_counterclockwise(graph):
    x, y = purifier[0]
    for i in range(x-1, 0, -1):
        graph[i][0] = graph[i-1][0]
    for i in range(C-1):
        graph[0][i] = graph[0][i+1]
    for i in range(x):
        graph[i][-1] = graph[i+1][-1]
    for i in range(C-1, 0, -1):
        graph[x][i] = graph[x][i-1]

def purify_clockwise(graph):
    x, y = purifier[1]
    for i in range(x+1, R-1):
        graph[i][0] = graph[i+1][0]
    for i in range(C-1):
        graph[-1][i] = graph[-1][i+1]
    for i in range(R-1, x, -1):
        graph[i][-1] = graph[i-1][-1]
    for i in range(C-1, 0, -1):
        graph[x][i] = graph[x][i-1]

for t in range(T):
    dust = [[0] * C for _ in range(R)]

    # 확산
    graph_copy = copy.deepcopy(A)
    for i in range(R):
        for j in range(C):
            defuse(i, j, graph_copy)
    # 순환
    purify_clockwise(dust)
    purify_counterclockwise(dust)

    for x, y in purifier:
        dust[x][y] = -1
    
    A = copy.deepcopy(dust)

answer = 0
for i in range(len(dust)):
    answer += sum(dust[i])
print(answer + 2)