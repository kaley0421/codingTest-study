# ---------------------------------------------------- 1트
# 1. 최단 경로 찾기 -> 해당 경로들을 graph 에서 제외 -> 최단 경로 길이 다시 찾기 로 푸려고 시도
# 2. 찾은 최단 경로들을 graph 에서 어떻게 지워줘야 할지 모르겠다. 구글링 후 보완 예정..
# ----------------------------------------------------
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

        for next, cost in graph[cur]:
            if dist + cost < distance[next]:
                heapq.heappush(q,(dist+cost, next))
                distance[next] = dist+cost
                for p in path[cur]: path[next].append(p)
                path[next].append(cur)

while True:
    n,m = map(int,input().split())

    if n == 0 and m == 0: break

    s,r = map(int,input().split())

    graph = [[] for _ in range(n)]
    distance = [1e9] * n
    path = [[] for _ in range(n)]    

    for _ in range(m):
        u,v,p = map(int,sys.stdin.readline().split())
        graph[u].append((v,p))
    
    dijkstra(s)

    # print("--  before graph: ")
    # for i in range(n):
    #     print(i, " graph")
    #     print(graph[i])

    # 최단 경로 찾기
    for i in range(n):
        print("-- path to ", i)
        print(path[i])
        for i in range(len(path[i])-1):
            _from = path[i]
            _to = path[i+1]

            graph[_from].remove((_to,graph))
        
    # print("--  after graph: ")
    # for i in range(n):
    #     print(i, " graph")
    #     print(graph[i])
    
    print("============================= case end")

    # 위의 경로들을 graph 에서 제외



    # 최단 경로 길이 찾기