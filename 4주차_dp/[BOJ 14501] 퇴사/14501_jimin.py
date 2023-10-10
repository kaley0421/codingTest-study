'''
1. dp[i]: i일에 얻을 수 있는 이득의 최댓값
'''
n = int(input())
t = [0]
p = [0]
for _ in range(n):
    cost, gain = map(int,input().split())
    t.append(cost)
    p.append(gain)

dp = [0] * (n+1)
for i in range(1,n+1):
    if dp[i] == 0:              # 이전 일수에서 i일에 얻을 거라고 킵해논 이득이 없는경우
        dp[i] = dp[i-1]
        if t[i] == 1:           # 하루만에 수행 가능한 경우, 수행
            dp[i] += p[i]
        else:                   # 하루만에 수행 가능하지 않은 경우
            if i+t[i]-1>n: continue
            dp[i+t[i]-1] = max(dp[i+t[i]-1], dp[i]+p[i])       # t일 뒤에 해당 이득을 가져가는게 이득이면 keep 해두기 <- dp[i]+p[i]
    else:                       # 이전 일수에서 i일에 얻을 거라고 킵해논 이득이 있는경우
        dp[i] = max(dp[i-1],dp[i])              # 킵해논 이득값을 선택하거나 (dp[i] = dp[i]) / 선택 X (dp[i] = dp[i-1])
        if t[i] == 1 and dp[i] == dp[i-1]:      # 킵해둔 이득값을 선택하지 않고, i일에 들어오는 작업 수행
            dp[i] = dp[i-1] + p[i]              # 킵해논 이득을 선택하지 않았기에, 해당 일에 자유로움 -> t가 1인 경우, 해당 일에 작업 수행
        else:
            if i+t[i]-1>n: continue
            dp[i+t[i]-1] = max(dp[i+t[i]-1], dp[i-1]+p[i])     # t일 뒤에 i일의 작업을 수행(dp[i-1]+p[i]) 하는게 이득인지, 아닌지 판단

print(dp[n])