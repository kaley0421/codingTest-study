''' 1트 => 메모리 초과
'''
# n,m = map(int,input().split())

# dp = [[0]*(n+1) for _ in range(n+1)]

# for _ in range(m):
#     a,b,c = map(int,input().split())
#     dp[a][b] = max(dp[a][b],c)
#     dp[b][a] = max(dp[b][a],c)

# start,end = map(int,input().split())

# for k in range(1,n+1):
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             dp[i][j] = max(dp[i][j], min(dp[i][k], dp[k][j]))

# print(dp[start][end])


''' 2트 => 시간 초과 (bfs 사용)
'''
# import sys
# from collections import deque

# n,m = map(int,input().split())

# graph = [[] for _ in range(n+1)]

# for _ in range(m):
#     a,b,c = map(int,sys.stdin.readline().split())
#     graph[a].append((b,c))
#     graph[b].append((a,c))

# start,end = map(int,input().split())

# def bfs(start):
#     q = deque([(start)])
#     visited[start] = 1e9

#     while q:
#         cur = q.popleft()
#         for next,weight in graph[cur]:
#             if visited[cur] > visited[next]:
#                 visited[next] = min(weight, visited[cur])
#                 q.append(next)

# visited = [-1] * (n+1)
# bfs(start)
# print(visited[end])


''' 3트 => 답 참고 (bfs + 이분탐색 사용)
1. 가능한 모든 중량들을 이분탐색으로 찾는다.
2. 해당 중량일 때 start ~ end 까지 도달할 수 있는지 bfs 를 통해 확인한다.
'''
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

start,end = map(int,input().split())

def bfs(candi_weight):
    q = deque([start])
    visited = [False] * (n+1)
    visited[start] = True

    while q:
        cur = q.popleft()
        for next,weight in graph[cur]:
            if not visited[next] and weight >= candi_weight:
                visited[next] = True
                q.append(next)
    
    if visited[end] == True: return True
    else: return False

_min, _max = 1, 1e9
answer = 0
while _min <= _max:
    mid = (_min + _max) // 2

    if bfs(mid):
        answer = mid
        _min = mid + 1
    else:
        _max = mid - 1
print(int(answer))