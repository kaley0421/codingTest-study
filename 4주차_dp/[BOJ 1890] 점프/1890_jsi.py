# DP[x][y] = [x, y]로 오는 가짓수
N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * N for _ in range(N)]

DP[0][0] = 1

for i in range(N):
    for j in range(N):
        if L[i][j] == 0:
            continue
        for x, y in [(i + L[i][j], j), (i, j + L[i][j])]:
            if 0 <= x < N and 0 <= y < N:
                DP[x][y] += DP[i][j]

print(DP[-1][-1])

"""
N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * N for _ in range(N)]

DP[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            continue
        
        for k in range(1, 10):
            if j-k < 0 or N <= j-k:
                break
            if L[i][j-k] == k:
                DP[i][j] += DP[i][j-k]

        for k in range(1, 10):
            if i-k < 0 or N <= i-k:
                break
            if L[i-k][j] == k:
                DP[i][j] += DP[i-k][j]
                
print(DP[-1][-1])
"""