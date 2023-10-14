'''
[ 14501 번 문제의 시간 효율 개선하기 ]
- 기존 14501 풀이에서 입력부분만 sys.stdin.readline() 으로 바꿨더니 성공. 뭐지 ??
    : dp[i] 값 갱신 시 dp[0] ~ dp[i-1] 를 순회하지 않고 오로지 dp[i-1] 값만 참고해서 갱신하도록 해야 통과인듯.
'''
import sys

n = int(input())
t = [0]
p = [0]
for _ in range(n):
    cost, gain = map(int,sys.stdin.readline().split())
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


'''
[ 코드 개선 ]
1. i일에 얻을 거라고 킵해둔 이득이 있는경우/없는경우 를 굳이 나눌 필요 X
    : 있으면 dp[i-1] 과 dp[i] 중 큰 값을 택할 거고, 없으면 dp[i-1] 값을 가져올 것
2. t[i] 가 1인 경우/아닌경우 를 굳이 나눌 필요 X
    : t[i] 가 1인 경우, dp[i] = max(dp[i], dp[i-1]+p[i]) 가 될 것
'''
import sys

n = int(input())
t = [0]
p = [0]
for _ in range(n):
    cost, gain = map(int,sys.stdin.readline().split())
    t.append(cost)
    p.append(gain)

dp = [0] * (n+1)

for i in range(1,n+1):
    dp[i] = max(dp[i-1],dp[i])
    if i+t[i]-1 > n: continue
    dp[i+t[i]-1] = max(dp[i+t[i]-1], dp[i-1]+p[i])

print(dp[n])