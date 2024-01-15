import sys

input=sys.stdin.readline

N=int(input())
L=[list(map(int, input().split())) for _ in range(N)]
answer=[0,0,0]

def dfs(n, x, y):
    global answer
    
    if n==1:
        answer[L[x][y]+1] += 1
        return
    check=True
    
    for dx in [0, n//3, 2*n//3]:
        if n != L[x+dx][y:y+n].count(L[x][y]):
            check = False
            break
    
    if check:
        answer[L[x][y]+1] += 1
        return
    
    for dx in [0, n//3, 2*n//3]:
        for dy in [0, n//3, 2*n//3]:
            dfs(n//3, x+dx, y+dy)

dfs(N, 0, 0)
print(answer[0])
print(answer[1])
print(answer[2])