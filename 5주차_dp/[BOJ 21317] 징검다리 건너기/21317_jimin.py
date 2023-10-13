'''
1. dp[i][0]: 가장 큰 점프를 안 쓰고 i번째 돌까지 도달할 수 있는 에너지 최소값
   dp[i][1]: 가장 큰 점프를 어디선가 쓴 경우 i번째 돌까지 도달할 수 있는 에너지 최소값
'''
n = int(input())
small_jump, big_jump = [], []
for _ in range(n-1):
    s,b = map(int,input().split())
    small_jump.append(s)
    big_jump.append(b)
k = int(input())

dp = [[1e9] * 2 for _ in range(n)]
dp[0][0], dp[0][1] = 0, 0

# dp[0] 채우기
for i in range(n):
    if i+1 < n:
        dp[i+1][0] = min(dp[i+1][0], dp[i][0]+small_jump[i])
    if i+2 < n:
        dp[i+2][0] = min(dp[i+2][0], dp[i][0]+big_jump[i])

# dp[1] 을 이용해서 '어딘가에서 가장 큰 점프 쓰는 경우' 나올 수 있는 dp[n][1] 의 최소값 찾기
temp_min = 1e9
for jump_spot in range(n-3):
    for i in range(n): dp[i][1] = 1e9

    dp[jump_spot][1] = dp[jump_spot][0]
    dp[jump_spot+3][1] = dp[jump_spot][1]+k
    for j in range(jump_spot+3,n):
        if j+1 < n:
            dp[j+1][1] = min(dp[j+1][1], dp[j][1]+small_jump[j])
        if j+2 < n:
            dp[j+2][1] = min(dp[j+2][1], dp[j][1]+big_jump[j])
    
    temp_min = min(temp_min, dp[n-1][1])
        
print(min(dp[n-1][0], temp_min))