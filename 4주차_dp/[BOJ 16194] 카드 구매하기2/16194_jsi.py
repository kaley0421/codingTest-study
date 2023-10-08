INF = 1e9

N = int(input())
P = [0] + list(map(int, input().split()))
DP = [INF] * (N + 1)

DP[0] = 0

for i in range(N + 1):
    for j in range(i + 1):
        DP[i] = min(DP[i], DP[i-j] + P[j])

print(DP[N])