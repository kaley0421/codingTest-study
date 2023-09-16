# ---------------------------------------------------- 플로이드
# import sys

# n,m,r = map(int,input().split())
# items = [0] + list(map(int,input().split()))

# INF = int(1e9)

# graph = [[INF] * (n+1) for _ in range(n+1)]
# for i in range(1,n+1):
#     graph[i][i] = 0

# for _ in range(r):
#     a,b,l = map(int,sys.stdin.readline().split())
#     graph[a][b] = l
#     graph[b][a] = l

# for k in range(1,n+1):
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# answer = 0
# for start in range(1,n+1):
#     temp = items[start]
#     for node in range(1,n+1):
#         if 0 < graph[start][node] <= m:
#             temp += items[node]
#     answer = max(answer,temp)

# print(answer)


# ---------------------------------------------------- 다익스트라 => 시간 효율 훨씬 굳.
import sys
import heapq

n,m,r = map(int,input().split())
items = [0] + list(map(int,input().split()))

INF = 1e9

graph = [[] for _ in range(n+1)]
for _ in range(r):
    a,b,l = map(int,sys.stdin.readline().split())
    graph[a].append((b,l))
    graph[b].append((a,l))

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
                heapq.heappush(q,(dist + cost, next))

answer = 0
for start in range(1,n+1):
    distance = [INF] * (n+1)
    dijkstra(start)

    temp = items[start]
    for i in range(1,n+1):
        if 0 < distance[i] <= m:
            temp += items[i]

    answer = max(answer, temp)

print(answer)
