import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

N = int(input())

def dijkstra(start):
    H = []

    distance[start] = 0
    heapq.heappush(H, (0, start, 0))
    
    while H:
        dist, node, order = heapq.heappop(H)

        if dist < distance[node]:
            continue

        for node_start, node_cost in graph[node]:
            cost = dist + node_cost

            if cost < distance[node_start]:
                distance[node_start] = cost
                heapq.heappush(H, (cost, node_start, order + 1))


for i in range(N):
    n, d, c = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    dijkstra(c)
    
    num, time = 0, 0
    for j in range(1, n + 1):
        if distance[j] == INF:
            continue
        num += 1
        time = max(time, distance[j])
    
    print(num, time)