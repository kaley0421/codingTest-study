''' 1트 => 3% 에서 시간초과. 1차원 dp 로 바꿔볼것.
'''
import sys

n,k = map(int,input().split())
coins = [0]
for _ in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))

coins.sort()

dp = [[0] * (k+1) for _ in range(n+1)]
dp[1][0] = 1
for j in range(1,k+1):
    if j % coins[1] == 0: dp[1][j] = 1

for i in range(2,n+1):
    dp[i][0] = 1
    for j in range(1,k+1):
        t = 0
        while coins[i] * t <= j:
            dp[i][j] += dp[i-1][j-coins[i]*t]
            t += 1
        
print(dp[n][k])