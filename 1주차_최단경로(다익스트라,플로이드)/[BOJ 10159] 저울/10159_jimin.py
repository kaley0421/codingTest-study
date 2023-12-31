import sys

INF = 1e9

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i] = 0

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[b][a] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1,n+1):
    answer = 0
    for j in range(1,n+1):
        if graph[i][j] == INF and graph[j][i] == INF:
            answer += 1
    print(answer)