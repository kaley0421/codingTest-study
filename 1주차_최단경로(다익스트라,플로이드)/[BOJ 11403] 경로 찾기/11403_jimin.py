n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k]>0 and graph[k][j]>0:
                if graph[i][j] == 0:
                    graph[i][j] = graph[i][k] + graph[k][j]
                else:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] > 0: print("1",end=" ")
        else: print("0", end=" ")
    print()