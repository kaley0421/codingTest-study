N, r, c = map(int, input().split())
answer = 0

def dfs(n, x, y):
    global answer

    if n == 1:
        answer += 2*x+y
        return

    quarter = 2**((n-1)*2)

    if x < 2**(n-1):
        if y < 2**(n-1):
            dfs(n-1, x, y)
        else:
            answer += quarter
            dfs(n-1, x, y-2**(n-1))
    else:
        if y < 2**(n-1):
            answer += 2*quarter
            dfs(n-1, x-2**(n-1), y)
        else:
            answer += 3*quarter
            dfs(n-1, x-2**(n-1), y-2**(n-1))
dfs(N, r, c)
print(answer)