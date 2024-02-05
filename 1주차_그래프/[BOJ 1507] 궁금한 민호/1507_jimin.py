import copy

n = int(input())
graph= []
for _ in range(n):
    graph.append(list(map(int,input().split())))
origin = copy.deepcopy(graph)

for k in range(n):
    for start in range(n):
        for end in range(n):
            if start == end: continue
            if k == start or k == end: continue
            if origin[start][end] == origin[start][k] + origin[k][end]:
                graph[start][end] = 0
                graph[end][start] = 0
            elif origin[start][end] > origin[start][k] + origin[k][end]:
                print(-1)
                exit()

answer = 0
for i in range(n-1):
    for j in range(i+1,n):
        answer += graph[i][j]

print(answer)