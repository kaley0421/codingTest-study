from collections import deque
import sys

p,w = map(int,input().split())
start,end = map(int,input().split())

graph = [[] for _ in range(p)]

for _ in range(w):
    s,e,cost = map(int,sys.stdin.readline().split())
    graph[s].append((e,cost))
    graph[e].append((s,cost))

def bfs(start):
    q = deque([start])
    visited[start] = 1e9

    while q:
        cur = q.popleft()

        for _next, cost in graph[cur]:
            next_cost = min(visited[cur], cost)
            if visited[_next] == -1:
                visited[_next] = next_cost
                q.append(_next)
            else:
                if next_cost > visited[_next]:
                    visited[_next] = next_cost
                    q.append(_next)

visited = [-1] * (p)
bfs(start)
print(visited[end])           