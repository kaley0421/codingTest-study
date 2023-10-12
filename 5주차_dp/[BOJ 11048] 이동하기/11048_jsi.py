N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * M for _ in range(N)]

DP[0][0] = L[0][0]

for i in range(N):
    for j in range(M):
        for ni, nj in [(i-1, j-1), (i-1, j), (i, j-1)]:

            if 0 <= ni < N and 0 <= nj < M:
                DP[i][j] = max(DP[i][j], DP[ni][nj] + L[i][j])

print(DP[-1][-1])