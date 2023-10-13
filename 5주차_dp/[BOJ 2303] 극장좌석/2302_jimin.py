n = int(input())
m = int(input())
vips = []
for _ in range(m):
    vips.append(int(input()))

dp = [0] * (n+1)
if n >= 1: dp[1] = 1
if n >= 2: dp[2] = 2
for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]

blanks = []
temp = 0
for i in range(1,n+1):
    if i not in vips:
        temp += 1
    else:
        if temp > 0:
            blanks.append(temp)
            temp = 0
if temp > 0: blanks.append(temp)

answer = 1
for blank in blanks:
    answer *= dp[blank]
print(answer)