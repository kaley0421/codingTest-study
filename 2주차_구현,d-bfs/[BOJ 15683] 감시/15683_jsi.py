# 개수 적으니까 완전탐색??
# dfs 기능 명시
# dfs(level, graph)은 level번째 카메라부터 끝까지 감시 범위를 graph에 담음
# list.copy()를 하더라도 원조 아이템에 대해선 연동됨
import copy, sys

input = sys.stdin.readline

N, M = map(int, input().split())
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
answer = int(1e9)

L = []
camera = []
direction = [
    [], 
    [[UP], [DOWN], [LEFT], [RIGHT]], 
    [[UP, DOWN], [LEFT, RIGHT]],
    [[UP, RIGHT], [RIGHT, DOWN], [DOWN, LEFT], [LEFT, UP]],
    [[LEFT, UP, RIGHT], [UP, RIGHT,DOWN], [RIGHT, DOWN, LEFT], [DOWN, LEFT, UP]],
    [[UP, DOWN, LEFT, RIGHT]]
    ]

# [x][y]]에서 dir 방향으로 쏜다면
def shoot(x, y, dir, graph):
    while True:
        if dir == UP: x -= 1
        elif dir == DOWN: x += 1
        elif dir == LEFT: y -= 1
        elif dir == RIGHT: y += 1

        if not (0 <= x < N and 0 <= y < M) or graph[x][y] == 6:
            break
        if graph[x][y] <= 0:
            graph[x][y] = -1

def get_blind_spots(graph):
    cnt = 0
    for i in range(len(graph)):
        cnt += graph[i].count(0)

    return cnt

for i in range(N):
    L.append(list(map(int, input().split())))
    for j in range(M):
        if 0 < L[i][j] < 6:
            camera.append([i, j, L[i][j]])

# dfs(level)은 level번째 카메라부터 끝까지 감시 범위를 L에 담음
def dfs(level, graph):
    global L

    if level == len(camera):
        if get_blind_spots(graph) < get_blind_spots(L):
            L = graph
        return

    x, y, num = camera[level]

    for dir in direction[num]:
        graph_copy = copy.deepcopy(graph)
        for d in dir:
            shoot(x, y, d, graph_copy)
        dfs(level + 1, graph_copy)

dfs(0, L)
print(get_blind_spots(L))

"""
for i in range(5, 0, -1):
    for x, y in camera[i]:
        cnt, dir = 1e9, []
        for k in direction[i]:
            L_copy = copy.deepcopy(L)
            for l in k:
                shoot(x, y, l, L_copy)
            temp = count(L_copy)
            if temp < cnt:
                cnt, dir = temp, k

        # 사각지대가 가장 작은 방향으로 저장
        for k in dir:
            shoot(x, y, k, L)
print(count(L))
"""