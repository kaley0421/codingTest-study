n,m = map(int,input().split())

dp = [0] * 101
dp[1] = 1

for i in range(2,101):
    dp[i] = dp[i-1] * i

print(dp[n]//(dp[n-m]*dp[m]))