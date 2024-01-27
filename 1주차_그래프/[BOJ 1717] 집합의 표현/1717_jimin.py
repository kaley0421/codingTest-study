import sys
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b: parent[b] = a
    else: parent[a] = b

parent = [i for i in range(n+1)]

for _ in range(m):
    command, a, b = map(int, sys.stdin.readline().split())
    if command == 0:
        union(a,b)
    else:
        a = find(a)
        b = find(b)
        if a == b: print("YES")
        else: print("NO")