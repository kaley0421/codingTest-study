N = int(input())
T, P = [], []
DP = [0] * (N + 1)

for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)


for i in range(N):
    for j in range(i + T[i], N + 1):
        if DP[j] < DP[i] + P[i]:
            DP[j] = DP[i] + P[i]

print(DP[-1])