# 모두 1 -> bfs, dfs 가능 + dijkstra도 가능
# 근데 dfs 못 하겠어ㅜㅜ

# bfs
from collections import deque

n = int(input())
start_x, start_y = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start_x, start_y):
    q = deque([start_x])
    visited[start_x] = 0

    while q:
        x = q.popleft()
        
        if x == start_y:
            return visited[x]

        for nx in graph[x]:
            if visited[nx] == 0:
                visited[nx] = visited[x] + 1
                q.append(nx)
    return -1

print(bfs(start_x, start_y))

# dijkstra
"""
import heapq

INF = 1e9
n = int(input())
start_x, start_y = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append((y, 1))
    graph[y].append((x, 1))


def dijkstra(start_x):
    H = []
    heapq.heappush(H, (0, start_x))
    distance[start_x] = 0

    while H:
        dist, now = heapq.heappop(H)

        if distance[now] < dist:
            continue

        for node, node_dist in graph[now]:
            cost = node_dist + dist

            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(H, (cost, node))

dijkstra(start_x)
print(distance[start_y] if distance[start_y] != INF else -1)
"""
