import sys
import heapq
INF = 1e9

n,m,x = map(int,input().split())

graph = [[] for _ in range(n+1)]
distance = [1e9] * (n+1)

student_cost = [0] * (n+1)

for _ in range(m):
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

# 가는길
for start in range(1,n+1):
    if start != x:
        distance = [1e9] * (n+1)
        dijkstra(start)
        student_cost[start] = distance[x]

# 오는길    
distance = [1e9] * (n+1)
dijkstra(x)
for home in range(1,n+1):
    if home != x:
        student_cost[home] += distance[home]

print(max(student_cost))