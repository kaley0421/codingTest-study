INF = 1e9

v,e = map(int,input().split())
graph = [[INF]*v for _ in range(v)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a-1][b-1] = c

for k in range(v):
    for a in range(v):
        for b in range(v):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

answer = 1e9
for start in range(v):
    answer = min(answer, graph[start][start])
if answer == 1e9: print(-1)
else: print(answer)