import copy

N, S, M = map(int, input().split())
L = [0] + list(map(int, input().split()))

def solution():
    prev, cur = [S], []
    
    for i in range(1, N+1):
        for vol in prev:
            for new_vol in [vol - L[i], vol + L[i]]:
                if 0 <= new_vol <= M and new_vol not in cur:
                    cur.append(new_vol)

        if len(cur) == 0:
            print(-1)
            return
        prev = copy.deepcopy(cur)
        cur.clear()

    print(max(prev))
solution()

"""
N, S, M = map(int, input().split())
L = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
graph[0].append(S)

def solution():
    for i in range(1, N+1):
        for vol in graph[i-1]:
            for new_vol in [vol - L[i], vol + L[i]]:
                if 0 <= new_vol <= M:
                    graph[i].append(new_vol)
        if len(graph[i]) == 0:
            print(-1)
            return

    print(max(graph[-1]))

solution()"""

# 메모리 초과
"""
from collections import deque

N, S, M = map(int, input().split())
L = list(map(int, input().split()))

def bfs(start):
    q = deque([(start, 0)])
    answer = -1

    while q:
        vol, idx = q.popleft()

        if idx == len(L):
            answer = max(answer, vol)
            if answer == M: break
            continue

        for new_vol in [vol - L[idx], vol + L[idx]]:
            if 0 <= new_vol <= M:
                q.append((new_vol, idx + 1))
    return answer

print(bfs(S))
"""