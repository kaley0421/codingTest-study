import sys
from collections import deque

V = int(input())
distance = [[] for _ in range(V+1)]

for i in range(1, V + 1):
    temp = deque(list(map(int, sys.stdin.readline().rstrip().split())))
    x = temp.popleft()

    while temp[0] != -1:
        y, dist = temp.popleft(), temp.popleft()
        distance[x].append([y, dist])

def bfs(start):
    q = deque([(start, 0)])
    answer = [start, 0]

    visited = [False] * (V+1)
    visited[start] = True
    

    while q:
        node, dist = q.popleft()

        for y, y_dist in distance[node]:
            if not visited[y]:
                visited[y] = True
                q.append((y, dist + y_dist))

                if answer[1] < dist + y_dist:
                    answer = [y, dist + y_dist]

    return answer

node, dist = bfs(1)
print(bfs(node)[1])

"""
# 시간 초과
# 메모리를 적게 쓰려고 반복 연산을 했나 봄
from collections import deque

INF = 1e9
V = int(input())
distance = [[] for _ in range(V+1)]

for i in range(1, V + 1):
    temp = deque(list(map(int, input().split())))
    x = temp.popleft()

    while temp[0] != -1:
        y, dist = temp.popleft(), temp.popleft()
        distance[i].append([y, dist])

def bfs(start_x):
    q = deque([(start_x, start_x)])
    visited = [-1] * (V+1)
    visited[start_x] = 0

    while q:
        x, y = q.popleft()
        
        for ny, dist in distance[y]:
            if visited[ny] == -1:
                visited[ny] = dist + visited[y]
                q.appendleft((y, ny))

    return max(visited)

answer = 0

for x in range(1, V+1):
    if len(distance[x]) != 0:
        answer = max(answer, bfs(x))
print(answer)

"""

"""
# 메모리초과
# 다익스트라라서 이차원 배열 때문인 듯
from collections import deque

INF = 1e9
V = int(input())
distance = [[INF] * (V+1) for _ in range(V+1)]

for i in range(1, V + 1):
    temp = deque(list(map(int, input().split())))
    x = temp.popleft()

    while temp[0] != -1:
        y, dist = temp.popleft(), temp.popleft()
        distance[x][y] = dist

for i in range(1, V+1):
    distance[i][i] = 0

def dijkstra():
    for v in range(1, V+1):
        for x in range(1, V+1):
            for y in range(1, V+1):
                distance[x][y] = min(distance[x][y], distance[x][v] + distance[v][y])
dijkstra()
answer = 0
for i in range(1, V+1):
    for j in range(1, V+1):
        if distance[i][j] != INF:
            answer = max(answer, distance[i][j])

print(answer)
"""