n = int(input())

dp = [1e9] * (n+1)
dp[1] = 0

for i in range(1,n+1):
    if i*3 <= n:
        dp[i*3] = min(dp[i*3], dp[i]+1)
    if i*2 <= n:
        dp[i*2] = min(dp[i*2], dp[i]+1)
    if i+1 <= n:
        dp[i+1] = min(dp[i+1], dp[i]+1)

print(dp[n])
if n>1:
    print(n, end = " ")
    before_num = n
    before_cnt = dp[n]
    for i in range(n-1,1,-1):
        if dp[i] == before_cnt - 1 and (i==before_num-1 or i==before_num/2 or i==before_num/3):
            print(i, end = " ")
            before_num = i
            before_cnt = dp[i]
print(1)