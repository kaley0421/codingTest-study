n, m = map(int, input().split())

DP = [[0] * (n+1) for _ in range(n+1)]

DP[1][0] = DP[1][1] = 1

for i in range(1, n+1):
    DP[i][0] = 1
    DP[i][i] = 1

for i in range(1, n+1):
    for j in range(1, i):
        DP[i][j] += DP[i-1][j-1] + DP[i-1][j]

print(DP[n][m])