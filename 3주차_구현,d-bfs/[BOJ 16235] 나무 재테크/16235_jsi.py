# 45%쯤에서 시간초과
import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
A = [[0] for _ in range(N + 1)]
tree = deque()
dead_tree = deque()
nourishment = [[5] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    A[i].extend(list(map(int, sys.stdin.readline().split())))

for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    tree.append([x, y, z])

def the_first_half(tree, nourishment):
    dead_tree = deque()
    _len = len(tree)

    for _ in range(_len):
        x, y, z = tree.pop()
        if nourishment[x][y] >= z:
            nourishment[x][y] -= z
            tree.appendleft([x, y, z+1])
        else:
            dead_tree.append([x, y, z])

    while dead_tree:
        x, y, z = dead_tree.popleft()
        nourishment[x][y] += z // 2

def the_second_half(tree, nourishment, A):
    dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
    _len = len(tree)

    for i in range(_len):
        x, y, z = tree[i]

        if z % 5 != 0: continue
        if z < 5: break
        
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if 0 < nx <= N and 0 < ny <= N:
                tree.append([nx, ny, 1])

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            nourishment[i][j] += A[i][j]

for _ in range(K):
    the_first_half(tree, nourishment)
    the_second_half(tree, nourishment, A)

    if len(tree) == 0: break

print(len(tree))


"""
# 시간 초과가 나는데 궁금해서 좀만 생각하다가 블로그 보고 싶음
import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
A = [[0] for _ in range(N + 1)]
tree = deque()
nourishment = [[5] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    A[i].extend(list(map(int, sys.stdin.readline().split())))

for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    tree.append([x, y, z])

def spring_and_summer(tree, nourishment):
    _len = len(tree)

    for _ in range(_len):
        x, y, z = tree.popleft()
        if nourishment[x][y] >= z:
            nourishment[x][y] -= z
            tree.append([x, y, z+1])
        else:
            nourishment[x][y] += z // 2

def fall(tree):
    dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
    _len = len(tree)

    for i in range(_len):
        x, y, z = tree[i]

        if z % 5 != 0:
            continue
        if z < 5:
            break
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if 0 < nx <= N and 0 < ny <= N:
                tree.appendleft([nx, ny, 1])

def winter(nourishment, A):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            nourishment[i][j] += A[i][j]

for i in range(K):
    spring_and_summer(tree, nourishment)
    fall(tree)
    winter(nourishment, A)

    if len(tree) == 0: break

print(len(tree))
"""