import sys

input = sys.stdin.readline

N = int(input())
graph = []
answer = [0, 0, 0]

for i in range(N):
    graph.append(list(map(int, input().split())))

def dfs(x, y, n):
    check = True
    if n == 1:
        answer[graph[x][y] + 1] += 1
        return
    
    for i in range(n):
        if graph[x + i][y:y+n].count(graph[x][y]) != n:
            check = False
            break

    if check == True:
        answer[graph[x][y] + 1] += 1
        return

    for i in range(x, x+n, n//3):
        for j in range(y, y+n, n//3):
            dfs(i, j, n//3)


dfs(0, 0, N)
print(' '.join(map(str, answer)))
