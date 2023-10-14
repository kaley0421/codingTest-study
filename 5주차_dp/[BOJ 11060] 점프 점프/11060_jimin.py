n = int(input())
_map = list(map(int,input().split()))

dp = [1e9]*n
dp[0] = 0

for i in range(n):
    for j in range(1,_map[i]+1):
        if i+j < n:
            dp[i+j] = min(dp[i+j], dp[i]+1)

if dp[-1] != 1e9:
    print(dp[-1])
else:
    print(-1)