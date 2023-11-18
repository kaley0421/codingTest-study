#start에 방문 처리 안 함

"""
from collections import deque

N, M = map(int, input().split())
_map = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    _map[a].append(b)
    _map[b].append(a)

def solve(start, visited, num):
    if num == 4:
        print(1)
        exit()
    
    for i in _map[start]:
        if visited[i] == 0:
            visited[i] = visited[start] + 1
            solve(i, visited, num + 1)
            visited[i] = 0
    return

for i in range(N):
    visited = [0] * N
    solve(i, visited, 0)

print(0)
"""

from collections import deque

N, M = map(int, input().split())
_map = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    _map[a].append(b)
    _map[b].append(a)

def solve(start, visited):
    if max(visited) >= 5:
        print(1)
        exit()
    
    for i in _map[start]:
        if visited[i] == 0:
            visited[i] = visited[start] + 1
            solve(i, visited)
            visited[i] = 0
    return

for i in range(N):
    visited = [0] * N
    visited[i] = 1
    solve(i, visited)

print(0)