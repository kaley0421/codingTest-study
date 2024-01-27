n,m,k = map(int,input().split())
money = list(map(int,input().split()))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        if money[a] < money[b]: parent[b] = a
        else: parent[a] = b
    
parent = [i for i in range(n)]

for _ in range(m):
    v,w = map(int,input().split())
    v -= 1
    w -= 1
    if v == w: continue
    if find(v) == find(w): continue
    union(v,w)

roots = set()
for i in range(n):
    roots.add(find(i))

answer = 0
for r in roots:
    answer += money[r]

if answer <= k: print(answer)
else: print("Oh no")