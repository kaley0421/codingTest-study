import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bfs(start, group):
    q = deque([start])
    visited[start] = group

    while q:
        node = q.popleft()

        for i in graph[node]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = -visited[node]
            elif visited[i] == visited[node]:
                return False
    return True

def dfs(start, group):
    visited[start] = group

    for i in graph[start]:
        if visited[i] == 0:
            answer = dfs(i, -visited[start])
            if not answer:
                return False
        elif visited[i] == visited[start]:
            return False
    return True

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    answer = False

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1, V + 1):
        if visited[i] == 0:
            answer = dfs(i, 1)
            # answer = bfs(i, 1)
            if not answer:
                break
    
    print('YES' if answer else 'NO')
