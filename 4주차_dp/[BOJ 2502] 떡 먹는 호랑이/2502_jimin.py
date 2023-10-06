d,k = map(int,input().split())

def validate():
    for i in range(1,d-2):
        if dp[i] + dp[i+1] != dp[i+2]: return False
        if dp[i] > dp[i+1]: return False
    return True

dp = [0] * (d+1)
dp[d] = k

for before_cnt in range(k-1,0,-1):
    dp[d-1] = before_cnt
    for day in range(d-2,0,-1):
        dp[day] = dp[day+2]-dp[day+1]
        if dp[day] > dp[day+1] or dp[day] <= 0: break
    if validate() == True: break

print(dp[1])
print(dp[2])