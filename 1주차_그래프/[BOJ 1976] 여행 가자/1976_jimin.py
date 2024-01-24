'''
1. 두 노드의 루트노드가 같다면, 이어져 있다고 판단한다.
'''
n = int(input())
m = int(input())

parent = [i for i in range(n)]

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a < b: parent[b] = a
    else: parent[a] = b

for i in range(n):
    arr = list(map(int,input().split()))
    for j in range(n):
        if arr[j] == 1:
            union(parent,i,j)

arr = list(map(int,input().split()))
for i in range(m-1):
    a,b = arr[i]-1, arr[i+1]-1
    ra = find(parent,a)
    rb = find(parent,b)
    if ra != rb:
        print("NO")
        exit()
print("YES")