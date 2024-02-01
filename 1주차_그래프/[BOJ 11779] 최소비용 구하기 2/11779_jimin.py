import heapq
import sys

INF = 1e9

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
path = []
prev_node = [0] * (n+1)

for _ in range(m):
    v1,v2,cost = map(int,sys.stdin.readline().split())
    graph[v1].append((v2,cost))

start,end = map(int,input().split())

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist: continue

        for _next, _cost in graph[now]:
            cost = dist + _cost
            if cost < distance[_next]:
                distance[_next] = cost
                prev_node[_next] = now
                heapq.heappush(q, (cost, _next))

dijkstra(start)

path = [end]
now = end
while now != start:
    now = prev_node[now]
    path.append(now)
path.reverse()

print(distance[end])
print(len(path))
print(' '.join(map(str,path)))