n,m = map(int,input().split())
_map = []
for _ in range(n):
    _map.append(list(input()))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a<b: parent[b] = parent[a]
    else: parent[a] = parent[b]

parent = [i for i in range(n*m)]

answer = 0
for i in range(n):
    for j in range(m):
        _cur, _next = m*i+j, 0

        if _map[i][j] == 'D':
            if i == n-1:
                answer += 1
                continue
            _next = m*(i+1)+j
        elif _map[i][j] == 'U':
            if i == 0:
                answer += 1
                continue
            _next = m*(i-1)+j
        elif _map[i][j] == 'L':
            if j == 0:
                answer += 1
                continue
            _next = m*i+(j-1)
        else:
            if j == m-1:
                answer += 1
                continue
            _next = m*i+(j+1)
        
        union(_cur,_next)

roots = set()
for i in range(n*m):
    roots.add(find(i))
answer += len(roots)

print(answer)