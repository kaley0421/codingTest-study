import sys

input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())

graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    graph[i][i] = 0

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

def floyd():
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

floyd()

for i in range(1, N + 1):
    answer = 0
    for j in range(1, N + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            answer += 1
    print(N - answer)