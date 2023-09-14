import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    s, d, c = map(int, input().split())
    graph[s].append((d, c))

start, end = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0

    while q:
        node, dist = heapq.heappop(q)

        if distance[node] < dist:
            continue
        
        for i in graph[node]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                heapq.heappush(q, (i[0], cost))
                distance[i[0]] = cost


dijkstra(start)

print(distance[end])