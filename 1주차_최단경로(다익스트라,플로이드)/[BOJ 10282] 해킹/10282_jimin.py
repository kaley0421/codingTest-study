import heapq
import sys

INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist: continue

        for v in graph[now]:
            cost = dist + v[1]
            if cost < distance[v[0]]:
                distance[v[0]] = cost
                heapq.heappush(q,(cost,v[0]))

t = int(input())
for _ in range(t):
    n,d,c = map(int,sys.stdin.readline().split())

    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for _ in range(d):
        a,b,s = map(int,sys.stdin.readline().split())
        graph[b].append((a,s))

    dijkstra(c)

    answer = 0
    cnt = 0
    for d in distance:
        if d != INF:
            answer = max(answer, d)
            cnt += 1
    print(cnt, answer)