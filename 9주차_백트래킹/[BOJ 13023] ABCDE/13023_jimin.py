'''
[ 주의 ]
- 특정 경로 a를 탐색해나가는 중에는 visited = False 인 노드로만 가야 하지만,
    a 경로에서 백트랙 -> b 경로로 탐색할 때 a 경로에서 기존에 방문되었던 노드가 다시 한번 방문될 수 있기 때문에
    dfs 수행 후 visited[i] = False 로 바꿔주는 과정 필요.
- 단순 dfs 와 달리 모든 노드가 딱 한번씩만 방문되는게 아님!
'''
n,m = map(int,input().split())

graph = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v,depth):
    global flag

    visited[v] = True
   
    if depth == 4:
        print(1)
        exit()

    for i in graph[v]:
        if not visited[i]:
            dfs(i,depth+1)
            visited[i] = False

for i in range(n):
    visited = [False] * n
    dfs(i,0)
print(0)