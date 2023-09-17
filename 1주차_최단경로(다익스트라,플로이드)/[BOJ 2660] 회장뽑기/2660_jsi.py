from collections import deque

N = int(input())
INF = int(1e9)

graph = [[INF] * (N + 1) for _ in range(N + 1)]
distance = [INF] * (N + 1)

while True:
    a, b = map(int, input().split())
    
    if a == -1 and b == -1: break

    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, N + 1):
    graph[i][i] = 0

def floyd():
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

score = INF
L = []
floyd()

for i in range(1, N + 1):
    if INF not in graph[i][1:]:
        score = min(score, max(graph[i][1:]))

for i in range(1, N + 1):
    if INF not in graph[i][1:] and max(graph[i][1:]) == score:
        L.append(i)

print(score, len(L))
print(' '.join(map(str, L)))