import sys
from collections import deque

input = sys.stdin.readline

d = [[-1, 0], [0, -1], [1, 0], [0, 1]]
T = int(input().strip())


def BFS(y, x):
    q = deque()
    cnt = [[-1] * (w + 2) for _ in range(h + 2)]
    q.append([y, x])
    cnt[y][x] = 0

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ty = y + dy
            tx = x + dx
            if 0 <= ty < h + 2 and 0 <= tx < w + 2:
                if cnt[ty][tx] == -1:
                    if prison[ty][tx] == '.':
                        q.appendleft([ty, tx])
                        cnt[ty][tx] = cnt[y][x]
                    elif prison[ty][tx] == '#':
                        q.append([ty, tx])
                        cnt[ty][tx] = cnt[y][x] + 1

    return cnt


for _ in range(T):
    h, w = map(int, input().split())
    prison = [['.'] * (w + 2)]
    for i in range(h):
        prison.append(list('.' + input().strip() + '.'))
    prison.append(['.'] * (w + 2))
    start = []

    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if prison[i][j] == '$':
                start.append([i, j])
                prison[i][j] = '.'

    cnt1 = BFS(start[0][0], start[0][1])
    cnt2 = BFS(start[1][0], start[1][1])
    cnt3 = BFS(0, 0)

    ans = float('inf')
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if cnt1[i][j] != -1 and cnt2[i][j] != -1 and cnt3[i][j] != -1:
                if prison[i][j] == '.':
                    ans = min(ans, cnt1[i][j] + cnt2[i][j] + cnt3[i][j])
                elif prison[i][j] == '#':
                    ans = min(ans, cnt1[i][j] + cnt2[i][j] + cnt3[i][j] - 2)
    print(ans)

"""# 0-1 bfs
# 가중치가 있다면 + 1 and append
# 가중치가 없다면 유지 and appendleft
# 감옥 밖을 나가려면 테두리에 1씩 더함 -> 1만 더한 건 최소거리 때문?
# 왜 0, 0에서 시작하지? 상근이 출발 위치 어디에 써있지?

from collections import deque

N = int(input())

def is_door(x, y):
    return True if graph[x][y] == '#' else False

def bfs(start_x, start_y):
    visited = [[0] * (w + 2) for _ in range(h + 2)]
    visited[start_x][start_y] = 1

    q = deque()
    q.append([start_x, start_y])

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < h + 2 and 0 <= ny < w + 2:
                if is_door(nx, ny):
                    q.appendleft([nx, ny])
                    visited[nx][ny] = visited[x][y]
                elif graph[nx][ny] == '.' or graph[nx][ny] == '$':
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1

    return visited


for _ in range(N):
    h, w = map(int, input().split())
    graph = [['.'] * (w + 2) for _ in range(h + 2)]
    prisoner = []

    for i in range(h):
        L = list(input())
        for j in range(w):
            if L[j] == '*' or L[j] == '#':
                graph[i][j] = L[j]
            elif L[j] == '$':
                graph[i][j] = L[j]
                prisoner.append([i, j])

    visited_1 = bfs(prisoner[0][0], prisoner[0][1])
    visited_2 = bfs(prisoner[1][0], prisoner[1][1])
    visited_3 = bfs(0, 0)

    answer = int(1e9)
    
    for i in range(1, h + 1):
        for j in range(1, w + 2):
            if visited_1[i][j] != 0 and visited_2[i][j] != 0 and visited_3[i][j] != 0:
                answer = min(answer, visited_1[i][j] + visited_2[i][j] + visited_3[i][j])

                if graph[i][j] == '#':
                    answer -= 2
    print(answer)"""