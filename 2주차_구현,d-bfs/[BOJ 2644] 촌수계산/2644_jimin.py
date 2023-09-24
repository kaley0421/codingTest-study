n = int(input())
start,target = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

m = int(input())
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v,step):
    global target

    if v == target:
        print(step)
        exit()

    visited[v] = True

    for next in graph[v]:
        if not visited[next]:
            dfs(next,step+1)

dfs(start,0)
print(-1)