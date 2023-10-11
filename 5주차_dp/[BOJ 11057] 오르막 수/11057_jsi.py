N = int(input())
DP = [[0] * 10 for _ in range(N + 1)]

for i in range(10):
    DP[0][i] = 1

for i in range(1, N + 1):
    for j in range(10):
        for k in range(j, 10):
            DP[i][j] += DP[i-1][k]
        DP[i][j] %= 10007

print(DP[-1][0])