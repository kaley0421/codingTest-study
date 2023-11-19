from copy import deepcopy

N, M = map(int, input().split())
_list = []

L, R, U, D = 0, 1, 2, 3

camera = []
visited = [[False] * M for _ in range(N)]

direction = [
    [],
    [[L], [R], [U], [D]],
    [[L, R], [U, D]],
    [[U, R], [R, D], [D, L], [L, U]],
    [[L, U, R], [U, R, D], [R, D, L], [D, L, U]],
    [[L, R, U, D]]
    ]

for i in range(N):
    _list.append(list(map(int, input().split())))

    for j in range(M):
        if 0 < _list[i][j] < 6:
            camera.append((i, j, _list[i][j]))

def get_blind_spots(graph):
    answer = 0
    for i in range(N):
        answer += graph[i].count(0)
    
    return answer

def shoot(x, y, direction, graph):
    while 0 <= x < N and 0 <= y < M and graph[x][y] != 6:
        if graph[x][y] == 0:
            graph[x][y] = -1

        if direction == L:
            y -= 1
        elif direction == R:
            y += 1
        elif direction == U:
            x -= 1
        elif direction == D:
            x += 1

num_blind_spots = 1e9

def dfs(idx, graph):
    global num_blind_spots

    if idx == len(camera):
        num_blind_spots = min(num_blind_spots, get_blind_spots(graph))
        return
    
    x, y, cam_num = camera[idx]

    for dir in direction[cam_num]:
        graph_copy = deepcopy(graph)

        for d in dir:
            shoot(x, y, d, graph_copy)
        dfs(idx+1, graph_copy)

dfs(0, _list)
print(num_blind_spots)