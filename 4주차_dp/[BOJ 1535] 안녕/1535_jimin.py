'''
[ 0-1 knapsack problem ]
- i 번째 물건을 넣냐 / 마냐 에 따른 최댓값 구하기
'''
n = int(input())
loss = [0] + list(map(int,input().split()))
gain = [0] + list(map(int,input().split()))

dp = [[0]*101 for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,101):
        if j - loss[i] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-loss[i]] + gain[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])