from collections import deque

n = int(input())
arr = list(map(int,input().split()))
delete = int(input())

start = 0
graph = [[] for _ in range(n)]
for i in range(n):
    parent = arr[i]
    if parent == -1:
        start = i               # 시작노드 지정
    else:
        if parent != delete and i != delete:    # 부모노드도 삭제되지 않았고, 현재노드도 삭제되지 않았다면 graph 에 경로 추가
            graph[parent].append(i)
visited = [False] * n

answer = 0

def bfs(start):
    global answer

    q = deque([start])
    visited[start] = True

    while q:
        cur = q.popleft()
    
        if len(graph[cur]) == 0: answer += 1    # 리프노드인 경우

        for next in graph[cur]:
            if not visited[next]:
                q.append(next)
                visited[next] = True

if start != delete: bfs(start)              # 시작노드가 삭제되지 않았다면, bfs 시작
print(answer)