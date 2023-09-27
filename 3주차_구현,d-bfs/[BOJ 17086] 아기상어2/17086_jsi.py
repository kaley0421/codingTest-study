from collections import deque

N, M = map(int, input().split())

graph, shark = [], []
dx, dy = [-1, 1, 0, 0, -1, 1, -1, 1], [0, 0, -1, 1, -1, -1, 1, 1]
result = -1

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        if graph[i][j] == 1:
            shark.append([i, j])

def bfs(start_x, start_y):
    q = deque([(start_x, start_y)])

    visited = [[0] * M for _ in range(N)]
    visited[start_x][start_y] = 0
    answer = 1e9

    while q:
        x, y = q.popleft()

        if graph[x][y] == 1:
            answer = min(answer, visited[x][y])
            break

        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return answer


for i in range(N):
    for j in range(M):
        result = max(result, bfs(i, j))

print(result)