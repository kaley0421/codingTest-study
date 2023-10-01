# 시간 초과가 나는데 궁금해서 좀만 생각하다가 블로그 보고 싶음
import sys

N, M, K = map(int, sys.stdin.readline().split())
A = [[0] for _ in range(N + 1)]
tree = []
dead_tree = []
nourishment = [[5] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    A[i].extend(list(map(int, sys.stdin.readline().split())))

for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    tree.append([x, y, z])

def spring(tree, nourishment):
    tree = sorted(tree, key=lambda x:(x[0], x[1], x[2]))

    for i in range(len(tree) -1, -1, -1):
        x, y, z = tree[i]
        if nourishment[x][y] >= z:
            nourishment[x][y] -= z
            tree[i][-1] += 1
        else:
            dead_tree.append([x, y, z])
            del tree[i]

def summer(dead_tree, nourishment):
    for i in range(len(dead_tree)):
        x, y, z = dead_tree[i]
        nourishment[x][y] += z // 2
        
    dead_tree = []

def fall(tree):
    dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1, 1], [-1, 0, 1, -1, 0, 1, -1, 0, 1]

    for i in range(len(tree)):
        x, y, z = tree[i]

        if z % 5 != 0:
            continue
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if 0 < nx <= N and 0 < ny <= N:
                tree.append([nx, ny, 1])

def winter(nourishment, A):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            nourishment[i][j] += A[i][j]

for i in range(K):
    spring(tree, nourishment)
    summer(dead_tree, nourishment)
    fall(tree)
    winter(nourishment, A)

    if len(tree) == 0: break

print(len(tree))