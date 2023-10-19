import sys
import heapq
from collections import deque

INF = 1e9
input = sys.stdin.readline

def bfs(now):
    q = deque([now])

    while q:
        n = q.pop()

        nlen = len(reversed_graph[n])

        for idx in range(nlen-1, -1, -1):
            pre, cost = reversed_graph[n][idx]
            if distance[pre] == distance[n] - cost:
                q.append(pre)
                del reversed_graph[n][idx]
    

def dijkstra(start, graph, distance):
    H = []
    heapq.heappush(H, (0, start))
    distance[start] = 0

    while H:
        dist, node = heapq.heappop(H)

        if distance[node] < dist:
            continue

        for node_end, node_cost in graph[node]:
            cost = dist + node_cost

            if cost < distance[node_end]:
                distance[node_end] = cost

                heapq.heappush(H, (cost, node_end))

while True:
    N, M = map(int, input().split())

    if N == 0 or M == 0:
        break

    S, D = map(int, input().split())

    graph = [[] for _ in range(N)]
    reversed_graph = [[] for _ in range(N)]
    distance = [INF] * (N)

    for _ in range(M):
        u, v, p = map(int, input().split())
        graph[u].append((v, p))
        reversed_graph[v].append((u, p))

    dijkstra(S, graph, distance)
    bfs(D)
    distance = [INF] * (N)
    dijkstra(D, reversed_graph, distance)
    
    print(distance[S] if distance[S] != INF else -1)