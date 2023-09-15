import sys

input = sys.stdin.readline

INF = int(1e9)
N = int(input())

graph = [[INF] * N for _ in range(N)]

for i in range(N):
    L = list(map(int, input().split()))
    for j in range(N):
        graph[i][j] = L[j] if L[j] == 1 else INF

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(N):
    for j in range(N):
        print(0 if graph[i][j] == INF else 1, end=' ')
    print()