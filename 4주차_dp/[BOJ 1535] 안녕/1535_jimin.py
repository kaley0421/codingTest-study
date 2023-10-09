'''
[ 0-1 knapsack problem ]
- i 번째 물건을 넣냐 / 마냐 에 따른 최댓값 구하기
Q.
1. 왜 dp[n][100] 아니고 dp[n][99]?
    : 체력이 0 이 되면 안되므로, 최대 쓸 수 있는 체력은 99 라서
2. j - loss[i] > 0 아니고 j - loss[i] >= 0 인 이유는?
    (체력 0 되면 죽어서 기쁨을 못 느낀다는 조건은 어디?)
    : j-loss[i] > 0 으로 했을 시 반례 => 1
                                    99
                                    20
    : j-loss[i] > 0 으로 하고, 답을 dp[n][100] 으로 출력해도 ok.
    : 어차피 dp[n][99] 를 출력하기 때문에 99 만큼의 체력을 다 써도 상관 없다는 의미?
      dp[n][100] 으로 출력하고 싶은 경우에는 쓸 수 있는 체력이 최대 100 이 아니고 99 라서 j-loss[i]>0 (>=1 과 같음) ?
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