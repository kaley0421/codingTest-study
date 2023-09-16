import heapq

INF = int(1e9)

n, m, r = map(int, input().split())
t = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

def dijkstra(start, graph, distance):
    H = []
    heapq.heappush(H, (0, start))
    distance[start] = 0
    
    while H:
        dist, node = heapq.heappop(H)

        if distance[node] < dist:
            continue

        for node_end, node_cost in graph[node]:
            cost = node_cost + dist

            if cost < distance[node_end]:
                distance[node_end] = cost
                heapq.heappush(H, (cost, node_end))

answer = 0

for start in range(1, n + 1):
    num_items = 0

    graph_new = graph.copy()
    distance = [INF] * (n + 1)

    dijkstra(start, graph_new, distance)

    for i in range(1, n + 1):
        if m < distance[i]:
            continue
        num_items += t[i]
    
    answer = max(answer, num_items)

print(answer)