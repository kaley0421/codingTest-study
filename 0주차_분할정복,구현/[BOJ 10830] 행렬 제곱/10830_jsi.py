N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def multiply(arr1, arr2):
    arr3 = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                arr3[i][j] += arr1[i][k] * arr2[k][j]
            arr3[i][j] %= 1000
    
    return arr3

def dfs(n, arr):
    if n == 1:
        return arr
    
    res = dfs(n//2, arr)

    if n % 2 == 0:
        return multiply(res, res)

    else:
        return multiply(multiply(res, res), arr)

answer = dfs(B, A)

for i in range(N):
    for j in range(N):
        print(answer[i][j]%1000, end=' ')
    print()