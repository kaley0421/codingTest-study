N = int(input())
A = list(map(int, input().split()))

DP = [1e9] * N
DP[0] = 0

for i in range(N):
    for j in range(1, A[i] + 1):
        if i + j >= N:
            break
        DP[i + j] = min(DP[i + j], DP[i] + 1)

print(DP[-1] if DP[-1] != 1e9 else -1)