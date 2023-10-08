'''
[ 0-1 knapsack problem ]
- i 번째 물건을 넣냐 / 마냐 에 따른 최댓값 구하기
Q.
1. 왜 dp[n][100] 아니고 dp[n][99]?
2. j - loss[i] > 0 아니고 j - loss[i] >= 0 인 이유는?
    (체력 0 되면 죽어서 기쁨을 못 느낀다는 조건은 어디?)
3. j 값이 '현재 체력' 을 뜻한다고 생각했는데, 아닌건가..?
    (dp[i][j] 는 'i번째 사람까지 고려, 현재체력 j' 일 때 얻을 수 있는 최대 이익 이라고 생각)
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
    print("dp[",i,"] :", dp[i])

print(dp[n][99])