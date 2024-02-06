import sys
import heapq

INF = 1e9

def dijkstra(start, distance):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0,start))

    while q:
        dist, cur = heapq.heappop(q)

        if dist > distance[cur]: continue

        for next,cost in graph[cur]:
            if distance[next] > dist+cost:
                distance[next] = dist+cost
                heapq.heappush(q, (dist+cost, next))

n,e = map(int,input().split())
graph = [[] for _ in range(n)]

for _ in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a-1].append((b-1,c))
    graph[b-1].append((a-1,c))

v1,v2 = map(int,input().split())
v1 -= 1
v2 -= 1

ans1, ans2 = 0, 0

distance = [INF] * n
dijkstra(0, distance)
ans1, ans2 = distance[v1], distance[v2]

distance_1 = [INF] * n
dijkstra(v1, distance_1)

distance_2 = [INF] * n
dijkstra(v2, distance_2)

ans1 += distance_1[v2]
ans1 += distance_2[n-1]
ans2 += distance_2[v1]
ans2 += distance_1[n-1]

answer = min(ans1, ans2)
if answer >= INF: print(-1)
else: print(answer)