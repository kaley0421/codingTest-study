# 거리기준
import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)
N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    H = []
    distance = [INF] * (N + 1)

    heapq.heappush(H, (0, start))
    distance[start] = 0

    while H:
        dist, node = heapq.heappop(H)

        if distance[node] < dist:
            continue

        for i in graph[node]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(H, (cost, i[0]))
    return distance

answer = -1

distance_go = dijkstra(X)

for i in range(1, N + 1):
    distance_back = dijkstra(i)
    answer = max(answer, distance_go[i] + distance_back[X])

print(answer)