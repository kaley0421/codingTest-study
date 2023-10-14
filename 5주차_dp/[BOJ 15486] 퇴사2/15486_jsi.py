import sys

input = sys.stdin.readline

N = int(input())
T, P = [0], [0]
DP = [0] * (N+1)

for i in range(N):
    t, p = map(int, input().split())

    T.append(t)
    P.append(p)

for i in range(1, N + 1):
    DP[i] = max(DP[i], DP[i-1])
    
    if i + T[i] - 1 < N + 1:
        DP[i + T[i] - 1] = max(DP[i + T[i] - 1], DP[i - 1] + P[i])

print(DP[-1])