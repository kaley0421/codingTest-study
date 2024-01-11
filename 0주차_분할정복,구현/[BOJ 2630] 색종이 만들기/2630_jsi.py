N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0]

def dfs(n, x, y):
    global answer

    if n == 1:
        answer[L[x][y]] += 1
        return
    
    _sum = 0
    for i in range(n):
        _sum += sum(L[x+i][y:y+n])
    
    if _sum == n*n:
        answer[1] += 1
        return
    elif _sum == 0:
        answer[0] += 1
        return

    for dx, dy in [(0, 0), (0, n//2), (n//2, 0), (n//2, n//2)]:
        dfs(n//2, x+dx, y+dy)

dfs(N, 0, 0)
print(answer[0])
print(answer[1])