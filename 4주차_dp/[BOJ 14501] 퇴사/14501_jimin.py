''' 예제 4에서 틀림. 원인 찾는 중.
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
    if dp[i] == 0:
        dp[i] = dp[i-1]
        if t[i] == 1:
            dp[i] += p[i]
        else:
            if i+t[i]-1>n: continue
            dp[i+t[i]-1] = max(dp[i+t[i]-1], dp[i]+p[i])
    else:
        dp[i] = max(dp[i-1],dp[i])
        if t[i] == 1:
            dp[i] = max(dp[i],p[i])
        else:
            if i+t[i]-1>n: continue
            dp[i+t[i]-1] = max(dp[i+t[i]-1], dp[i]+p[i])
    print("---- ")
    print("i: ", i)
    print("dp: ",dp)

print(dp[n])