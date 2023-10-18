from collections import deque

n,k = map(int,input().split())

visited = [-1] * (100001)

def bfs(start):
    global n,k

    q = deque([start])
    visited[start] = 0

    while q:
        cur = q.popleft()

        if cur == k:
            print(visited[cur])
            exit()

        if 0<=2*cur<100001 and visited[2*cur] == -1:
            q.append(2*cur)
            visited[2*cur] = visited[cur]

        if 0<=cur-1<100001 and visited[cur-1] == -1:
            q.append(cur-1)
            visited[cur-1] = visited[cur] + 1
        
        if 0<=cur+1<100001 and visited[cur+1] == -1:
            q.append(cur+1)
            visited[cur+1] = visited[cur] + 1

bfs(n)