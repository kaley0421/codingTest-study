# ---------------------------------------------------- 1트
# 1. 최단 경로 찾기 -> 해당 경로들을 graph 에서 제외 -> 최단 경로 길이 다시 찾기 로 푸려고 시도
# 2. 찾은 최단 경로들을 graph 에서 어떻게 지워줘야 할지 모르겠다. 구글링 후 보완 예정..
# ----------------------------------------------------
# import sys
# import heapq

# INF = 1e9

# def dijkstra(start):
#     q = []
#     heapq.heappush(q,(0,start))
#     distance[start] = 0

#     while q:
#         dist, cur = heapq.heappop(q)

#         if distance[cur] < dist: continue

#         for next, cost in graph[cur]:
#             if dist + cost < distance[next]:
#                 heapq.heappush(q,(dist+cost, next))
#                 distance[next] = dist+cost
#                 for p in path[cur]: path[next].append(p)
#                 path[next].append(cur)

# while True:
#     n,m = map(int,input().split())

#     if n == 0 and m == 0: break

#     s,r = map(int,input().split())

#     graph = [[] for _ in range(n)]
#     distance = [1e9] * n
#     path = [[] for _ in range(n)]    

#     for _ in range(m):
#         u,v,p = map(int,sys.stdin.readline().split())
#         graph[u].append((v,p))
    
#     dijkstra(s)

#     # print("--  before graph: ")
#     # for i in range(n):
#     #     print(i, " graph")
#     #     print(graph[i])

#     # 최단 경로 찾기
#     for i in range(n):
#         print("-- path to ", i)
#         print(path[i])
#         for i in range(len(path[i])-1):
#             _from = path[i]
#             _to = path[i+1]

#             graph[_from].remove((_to,graph))
        
#     # print("--  after graph: ")
#     # for i in range(n):
#     #     print(i, " graph")
#     #     print(graph[i])
    
#     print("============================= case end")

#     # 위의 경로들을 graph 에서 제외



#     # 최단 경로 길이 찾기


# ---------------------------------------------------- 2트 => 답 참고.
# 1. graph 저장에 dict 사용 -> remove 가 쉽다.
# 2. bfs 를 사용하며 최단경로를 역추적해서 해당 경로에 포함되는 경로들을 제거한다.
#    - 역추적 도중 출발노드 s 를 만난 경우에도 끝내지 않고 계속 탐색 (최단경로가 여러 개인 모든 경우를 찾기 위해 bfs 를 계속 돌린다.)
#    - 역추적 과정에서 'prev_v ~ v 까지의 비용 + prev_v 까지의 최단경로 = v 까지의 최단경로' 라면, 해당 prev_v ~ v 는 최단경로에 포함되는 경로이다.
# 3. 역추적을 위해서 reverse_graph 가 필요하다.
# ----------------------------------------------------
from collections import deque
import sys
import heapq

INF = 1e9

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, cur = heapq.heappop(q)

        if distance[cur] < dist: continue

        for i in graph[cur]:
            cost = dist + graph[cur][i]
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost,i))

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        v = q.popleft()

        if v == s: continue

        for prev_v, prev_c in reverse_graph[v]:
            if distance[prev_v] + graph[prev_v][v] == distance[v]:
                if (prev_v, v) not in removing:
                    removing.append((prev_v,v))
                    q.append(prev_v)

while True:
    n,m = map(int,input().split())

    if n == 0 and m == 0: break

    s,r = map(int,input().split())

    graph = [dict() for _ in range(n)]
    reverse_graph = [[] for _ in range(n)]    

    for _ in range(m):
        u,v,p = map(int,sys.stdin.readline().split())
        graph[u][v] = p
        reverse_graph[v].append((u,p))
    
    # 최단 경로 구하기
    distance = [INF] * n
    dijkstra(s)

    # 최단 경로에 포함되는 경로들을 찾아 graph 에서 제거
    removing = []
    bfs(r)
    for _from, _to in removing:
        del graph[_from][_to]
    
    # 최단 경로 다시 찾기
    distance = [INF] * n
    dijkstra(s)

    if distance[r] == INF: print(-1)
    else: print(distance[r])
