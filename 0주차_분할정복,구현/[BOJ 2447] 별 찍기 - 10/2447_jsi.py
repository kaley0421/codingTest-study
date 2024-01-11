N = int(input())
L = [[' '] * N for _ in range(N)]

def dfs(N, x, y):
    if N <= 3:
        for dx in range(0, 3):
            L[x+dx][y+0] = '*'
            if dx != 1:
                L[x+dx][y+1] = '*'
            L[x+dx][y+2] = '*'
        return
    
    for i in [0, N//3, 2*N//3]:
        dfs(N//3, x+i, y + 0)

        if i != N//3:
            dfs(N//3, x+i, y + N//3)

        dfs(N//3, x+i, y + 2*N//3)
dfs(N, 0, 0)

for i in range(N):
    print(''.join(L[i]))