n = int(input())
L = list(map(int, input().split()))
DP = [1] * n

for i in range(n):
    for j in range(i):
        if L[j] < L[i]:
            DP[i] = max(DP[i], DP[j] + 1)

print(max(DP))