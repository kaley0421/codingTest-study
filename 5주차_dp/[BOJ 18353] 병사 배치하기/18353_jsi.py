INF = 1e9

N = int(input())
L = [INF] + list(map(int, input().split()))
DP = [0] * (N + 1)

for i in range(1, N+1):
    for j in range(i):
        if L[i] < L[j]:
            DP[i] = max(DP[i], DP[j] + 1)

print(N - max(DP))