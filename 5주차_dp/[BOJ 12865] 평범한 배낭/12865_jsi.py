N, K = map(int, input().split())
W, V = [0], [0]
DP = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(N):
    w, v = map(int, input().split())
    
    W.append(w)
    V.append(v)

# DP[x][y] = x번 물건까지 있는데 무게의 한계가 y일 때
for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j >= W[i]:
            DP[i][j] = max(DP[i-1][j-W[i]] + V[i], DP[i-1][j])
        else:
            DP[i][j] = DP[i-1][j]

print(max(DP[-1]))