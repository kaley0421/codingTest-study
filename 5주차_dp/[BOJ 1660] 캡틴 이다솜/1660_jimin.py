''' 1트 => 시간초과
'''
# n = int(input())

# dp = [1e9] * (n+1)

# dp[1] = 1
# if n >= 2: dp[2] = 2
# if n >= 3: dp[3] = 3

# _sum, _cnt, num = 1, 1, 1
# while _sum <= n:
#     _cnt += 1
#     num += _cnt
#     _sum += num
#     if _sum <= n: dp[_sum] = 1

# for i in range(5,n+1):
#     for j in range(1,i):
#         dp[i] = min(dp[i], dp[j]+dp[i-j])

# print(dp[n])


''' 2트 => 답 참고
'''
n = int(input())

dp = [1e9] * (n+1)

dp[1] = 1
if n >= 2: dp[2] = 2
if n >= 3: dp[3] = 3

flag = []
_sum, _cnt, num = 1, 1, 1
while _sum <= n:
    _cnt += 1
    num += _cnt
    _sum += num
    if _sum <= n: 
        dp[_sum] = 1
        flag.append(_sum)

for i in range(5,n+1):
    for f in flag:
        if i > f:
            dp[i] = min(dp[i], dp[i-f]+1)
            
print(dp[n])