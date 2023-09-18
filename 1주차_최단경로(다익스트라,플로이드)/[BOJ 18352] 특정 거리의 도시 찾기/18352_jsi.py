# 가중치가 1임에도 다익스트라를 사용한 이유는?
# bfs는 최단거리 값 하나만 알아낼 수 있음

import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append((B, 1))

def dijkstra(start):
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
dijkstra(X)

answer = 0

for i in range(1, N + 1):
    if distance[i] == K:
        answer += 1
        print(i)
    elif i == N and answer == 0:
        print(-1)