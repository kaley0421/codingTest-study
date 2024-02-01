import heapq

n = int(input())
m = int(input())
MAP = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    MAP[start].append((end, cost))


start, end = map(int, input().split())
distance = [1e9] * (n+1)
prev_node = [0] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for node, node_dist in MAP[now]:
            cost = dist + node_dist

            if cost < distance[node]:
                distance[node] = cost
                prev_node[node] = now
                heapq.heappush(q, (cost, node))

route = [end]
now = end

dijkstra(start)

while now != start:
    now = prev_node[now]
    route.append(now)

print(distance[end])
print(len(route))
print(' '.join(map(str, reversed(route))))