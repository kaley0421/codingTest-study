import sys
input = sys.stdin.readline

def dfs(v):
    tree[v] = -2
    for i in range(n):
        if v == tree[i]:
            dfs(i)
            
n = int(input())
tree = list(map(int, input().split()))
erase = int(input())

dfs(erase)
cnt = 0

for i in range(n):
    if tree[i] != -2 and i not in tree:
        cnt+=1

print(cnt)