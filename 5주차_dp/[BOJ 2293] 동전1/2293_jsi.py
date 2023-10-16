n, k = map(int, input().split())
L = []
DP = [0] * (k + 1)

for _ in range(n):
    L.append(int(input()))

DP[0] = 1

for coin in L:
    for j in range(coin, k + 1):
        DP[j] += DP[j-coin]
    print(coin, DP)

print(DP[-1])