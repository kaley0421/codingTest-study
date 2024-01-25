import copy

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))
check = copy.deepcopy(graph)

for i in range(n):
    for j in range(n):
        if i == j: continue
        if graph[i][j] == 'N':
            for k in range(n):
                if graph[i][k] == 'Y' and graph[k][j] == 'Y':
                    check[i][j] = 'Y'

answer = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if check[i][j] == 'Y': cnt += 1
    answer = max(answer, cnt)
print(answer)