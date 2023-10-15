'''
[ 0-1 knapsack 기본 ] => 외우자 !!
1. dp[i][j]: i번째 물건까지 고려했을 때 & 현재 배낭에 담을 수 있는 최대 무게가 j일때의 최대 가치
2. j < w[i] 라면 i 번째 물건을 담지 못하므로, dp[i-1][j] 를 가져옴
3. j >= w[i] 라면 i 번째 물건을 담는 것 vs 담지 않는 것 중 최댓값 선택
'''
n,k = map(int,input().split())
w,v = [0], [0]
for _ in range(n):
    weight, value = map(int,input().split())
    w.append(weight)
    v.append(value)

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        if j < w[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v[i]+dp[i-1][j-w[i]],dp[i-1][j])

print(dp[n][k])