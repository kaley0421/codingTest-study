''' 1트 => dfs. 시간초과.
1. dfs 돌려서 자기자신으로 돌아올 수 없다면, 어느 팀에도 속하지 않는 것
'''
# import sys
# sys.setrecursionlimit(10**6)

# t = int(input())

# def dfs(cur, origin, visited):
#     global flag, cycles

#     visited[cur] = True
#     _next = choice[cur]
#     if visited[_next]:
#         if _next == origin:
#             flag = True
#             cycles.add(origin)
#             return
#     else:
#         dfs(_next, origin, visited)
#         if flag == True:
#             cycles.add(_next)

# for _ in range(t):
#     n = int(input())
#     choice = list(map(int,input().split()))
#     for i in range(n):
#         choice[i] -= 1
    
#     flag = False
#     cycles = set()
#     for start in range(n):
#         if choice[start] == start:
#             cycles.add(start)
#             continue
#         if start in cycles: 
#             continue
#         visited = [False] * n
#         dfs(start,start,visited)
    
#     print(n-len(cycles))    



''' 2트 => 답 참고.
1. dfs 돌리면서 사이클 발생 여부를 확인한다. (이미 방문했던 노드로 되돌아오는가?)
2. dfs 로 탐색해 나가는 경로를 path 리스트에 저장한다.
    - path -> '현재 탐색 중인 경로' 를 의미
3. x 노드에서 사이클이 발생했다면, path 에서 'x 노드 이후에 저장된 노드들' 이 사이클을 이루는 경로일 것이다. 
    - path[path.index(_next):] -> '_next 노드 이후에 저장된 노드들'
'''
import sys
sys.setrecursionlimit(10**6)

t = int(input())

def dfs(cur):
    global visited, path, answer

    visited[cur] = True
    path.append(cur)

    _next = choice[cur]

    if visited[_next]:               # 방문한 적 있는 노드이고,
        if _next in path:            # path 에 저장된 적 있는 노드라면, 사이클 발생
            answer -= len(path[path.index(_next):])
            return
    else:                            # 방문한 적 없는 노드인 경우, 계속 탐색
        dfs(_next)

for _ in range(t):
    n = int(input())
    choice = list(map(int,input().split()))
    for i in range(n):
        choice[i] -= 1
    
    path = []
    visited = [False] * n
    answer = n
    for start in range(n):
        if not visited[start]:
            path = []
            dfs(start)
    
    print(answer)   