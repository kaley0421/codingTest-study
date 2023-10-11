import copy

n = int(input())
a = list(map(int,input().split()))

dp = copy.deepcopy(a)

for i in range(1,n):
    for j in range(i-1,-1,-1):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + a[i])

print(max(dp))