import sys
import heapq
INF = int(1e9)

v,e = map(int,input().split())
start = int(input())

graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, cur = heapq.heappop(q)

        if distance[cur] < dist: continue

        for next,cost in graph[cur]:
            if dist + cost < distance[next]:
                distance[next] = dist + cost
                heapq.heappush(q,(dist+cost, next))

dijkstra(start)

for i in range(1,v+1):
    if distance[i] == INF: print("INF")
    else: print(distance[i])