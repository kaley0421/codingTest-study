n = int(input())
_map = list(map(int,input().split()))

dp = [1] * n

for i in range(1,n):
    for j in range(i-1,-1,-1):
        if _map[j] > _map[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(n-max(dp))