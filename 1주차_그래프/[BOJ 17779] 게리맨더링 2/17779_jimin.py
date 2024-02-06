n = int(input())
_map = []
for _ in range(n):
    _map.append(list(map(int,input().split())))

for x in range(n-2):
    for y in range(1,n-1):
        for d1 in range(1,n):
            for d2 
