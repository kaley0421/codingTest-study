# ---------------------------------------------------- 1트 => 43% 에서 틀림
# 1. bfs 돌리며 visited 배열에 해당 노드가 이분 집합 중 어디에 속하는지를 저장
# 2. bfs 탐색 도중 인접 노드와 같은 집합에 속하는 노드가 존재한다면, False 를 리턴
# [ 틀린 이유 ]
# - 단순히 1번 노드에서 bfs 를 시작하면, 1번 노드는 동떨어져 있고 나머지 연결된 노드들끼리 이분그래프가 아닌 경우를 판별 못함
# ----------------------------------------------------
# import sys
# from collections import deque

# k = int(input())

# def bfs(start):
#     q = deque([start])
#     visited[start] = 1

#     while q:
#         cur = q.popleft()

#         for next in graph[cur]:
#             if visited[next] == 0:
#                 q.append(next)
#                 visited[next] = -1 * visited[cur]
#             else:
#                 if visited[next] == visited[cur]:
#                     return False
#     return True

# for _ in range(k):
#     n,e = map(int,input().split())

#     graph = [[] for _ in range(n+1)]
#     visited = [0] * (n+1)
#     for _ in range(e):
#         u,v = map(int,sys.stdin.readline().split())
#         graph[u].append(v)
#         graph[v].append(u)

#     result = bfs(1)

#     if result == True: print("YES")
#     else: print("NO")


# ---------------------------------------------------- 2트
# 1. 노드들이 동떨어져 있는 경우를 고려해주기 위해, 모든 노드들이 방문 처리될 때까지 bfs 를 돌리도록 while 문 추가
# ----------------------------------------------------
import sys
from collections import deque

k = int(input())

def bfs(start):
    q = deque([start])
    visited[start] = 1

    while q:
        cur = q.popleft()

        for next in graph[cur]:
            if visited[next] == 0:
                q.append(next)
                visited[next] = -1 * visited[cur]
            else:
                if visited[next] == visited[cur]:
                    return False
    return True

for _ in range(k):
    n,e = map(int,input().split())

    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    visited[0] = -1
    for _ in range(e):
        u,v = map(int,sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    while 0 in visited:
        result = bfs(visited.index(0))
        if result == False: break

    if result == True: print("YES")
    else: print("NO")