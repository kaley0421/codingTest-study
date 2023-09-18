import sys
import heapq

INF = 1e9

n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append((b,1))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, cur = heapq.heappop(q)

        if distance[cur] < dist: continue

        for next, cost in graph[cur]:
            if dist+cost < distance[next]:
                heapq.heappush(q,(dist+cost, next))
                distance[next] = dist+cost

dijkstra(x)

if k not in distance: 
    print(-1)
else: 
    for i in range(1,n+1):
        if distance[i] == k: print(i)