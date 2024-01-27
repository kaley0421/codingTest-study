''' 1트 => 4% 에서 틀림. 이유 모르겠.
'''
# import sys
# sys.setrecursionlimit(10**6)

# n,m = map(int,input().split())

# if n == 1:
#     print(0)
#     exit()

# graph = [[0]*n for _ in range(n)]
# for _ in range(m):
#     a,b = map(int, sys.stdin.readline().split())
#     a -= 1
#     b -= 1
#     graph[a][b] = -1
#     graph[b][a] = 1
   
# def cnt(i, flag):   # i 번째 구슬보다 가벼운/무거운 구슬 개수 리턴
#     search = []
#     for j in range(n):
#         if graph[i][j] == flag:
#             search.append(j)

#     if len(search) == 0:
#         return 0
    
#     _cnt = len(search)
#     for s in search:
#         if _cnt >= (n+1)/2: 
#             return _cnt
#         _cnt += cnt(s, flag)
#     return _cnt

# answer = 0
# for i in range(n):
#     # i 번째보다 무거운 구슬 개수
#     if cnt(i,1) >= (n+1)/2: 
#         answer += 1
#     # i 번째보다 가벼운 구슬 개수
#     if cnt(i,-1) >= (n+1)/2:
#         answer += 1
# print(answer)



''' 2트 => 답 참고
1. d/bfs 를 이용하여 본인의 자식노드/손자노드가 n//2+1 개 이상이면 가운데에 올 수 없다.
2. 인접리스트를 다음과 같이 2개 사용한다.
    - 현재 구슬보다 무거운 구슬들을 저장하는 인접리스트 (hgraph)
    - 현재 구슬보다 가벼운 구슬들을 저장하는 인접리스트 (lgraph)
3. bfs 함수를 다음과 같이 2개 작성한다.
    - 현재 구슬보다 무거운 구슬들을 탐색 (hbfs)
    - 현재 구슬보다 가벼운 구슬들을 탐색 (lbfs)
'''
import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

hgraph = [[] for _ in range(n+1)]
lgraph = [[] for _ in range(n+1)]
criteria = n//2+1
answer = 0

for _ in range(m):
    h,l = map(int, sys.stdin.readline().split())
    hgraph[l].append(h)
    lgraph[h].append(l)

def hbfs(start):
    global answer
    visited = []
    q = deque([start])

    while q:
        cur = q.popleft()

        if cur not in visited:
            visited.append(cur)
            for next in hgraph[cur]: q.append(next)

    if len(visited) > criteria: 
        answer += 1
    
def lbfs(start):
    global answer
    visited = []
    q = deque([start])

    while q:
        cur = q.popleft()

        if cur not in visited:
            visited.append(cur)
            for next in lgraph[cur]: q.append(next)
    
    if len(visited) > criteria:
        answer += 1

for i in range(1,n+1):      # i 번째 구슬에 대해 조사
    hbfs(i)
    lbfs(i)

print(answer)