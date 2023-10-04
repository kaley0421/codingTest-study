# 지름길의 시작위치는 도착위치보다 작다 -> x에서 x+1은 1

import heapq

INF = 1e9
N, D = map(int, input().split())

graph = [[] for _ in range(D+1)]
distance = [INF] * (D+1)

for i in range(D):
    graph[i].append((i+1, 1))

for i in range(N):
    start, end, dist = map(int, input().split())
    if D < end:
        continue
    graph[start].append((end, dist))

def dijkstra(start):
    H = []
    heapq.heappush(H, (0, start))
    distance[start] = 0

    while H:
        dist, node = heapq.heappop(H)

        if distance[node] < dist:
            continue

        for ny, ny_dist in graph[node]:
            cost = dist + ny_dist

            if cost < distance[ny]:
                distance[ny] = cost
                heapq.heappush(H, (cost, ny))

dijkstra(0)
print(distance[-1])