import sys
import heapq
INF = 1e9

n = int(input())

graph = [[] for _ in range(n+1)]
while True:
    a,b = map(int,sys.stdin.readline().split())
    if a == -1 and b == -1: break
    graph[a].append((b,1))
    graph[b].append((a,1))

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

ans_score = 1e9
scores = [0]
for candi in range(1,n+1):
    distance = [0] + [INF] * (n)
    dijkstra(candi)
    score = max(distance)
    ans_score = min(ans_score,score)
    scores.append(score)

ans_arr = []
for i in range(1,n+1):
    if scores[i] == ans_score: ans_arr.append(i)

print(ans_score, len(ans_arr))
for ans in ans_arr:
    print(ans, end = " ")