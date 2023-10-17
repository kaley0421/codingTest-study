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


''' 2트 => 답 참고.
1. dp[price] += dp[price - coin] 의 의미
    ex. price = 5, coin = 2 라면 점화식은 dp[5] += dp[3]
        - 가치 2짜리 동전을 쓰면 채워야 하는 남은 금액은 3 이므로, dp[3] 을 확인
        - dp[3] 에는 1번째동전(가치 1), 2번째동전(가치 2)을 조합해 가치가 3이 되는 경우의 수가 저장되어 있을 것

2. dp[0] = 1 의 의미
    ex. price = 2, coin = 2 라면 점화식은 dp[2] += dp[0]
        - 2원짜리 동전을 하나만 써서 2를 만드는 경우를 고려 (dp[0])
'''
import sys

n,k = map(int,input().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))

coins.sort()

dp = [0] * (k+1)
dp[0] = 1               # 동전이 딱 한개만 쓰이는 경우를 고려

for coin in coins:
    print("--- coin: ", coin)
                                                # price: 채워야하는 가치 / coin: 현재 고려 중인 코인
    for price in range(coin,k+1):               # coin 을 사용할 수 있으려면 coin <= price 여야 하므로, range(coin ~) 으로 시작한다.
        dp[price] += dp[price-coin]
        print("price: ", price, " dp: ", dp)

    print("--- dp: ",dp)

print(dp[k])