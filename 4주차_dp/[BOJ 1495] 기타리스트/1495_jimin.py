''' 1트 => 재귀로 시도. 시간초과
'''
# import sys
# sys.setrecursionlimit(10**6)

# n,s,m = map(int,input().split())
# v = list(map(int,input().split()))

# dp = [0] * n

# answer = -1
# def dfs(vol,step):
#     global answer

#     if step == n:
#         answer = max(answer,vol)
#         return

#     if 0 <= vol+v[step] <= m:
#         dfs(vol+v[step],step+1)
#     if 0 <= vol-v[step] <= m:
#         dfs(vol-v[step],step+1)
#     return
    
# dfs(s,0)
# print(answer)


''' 2트 => dp 
1. 2차원 dp 테이블 생성
    - 행: n+1 (현재 몇번째 곡 연주중인지)
    - 열: m+1 (현재 단계에서 가능한 볼륨들 표시)
2. 마지막 행의 열을 보고 답 구하기 가능
    - '가능한 볼륨으로 표시되어 있는(1이 적혀있는) 열 중 가장 큰 열 번호' 구하기
'''
n,s,m = map(int,input().split())
v = [0] + list(map(int,input().split()))

dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(1,n+1):
    for j in range(m+1):
        if dp[i-1][j] != 0:
            if 0<=j-v[i]<=m: 
                dp[i][j-v[i]] = 1
            if 0<=j+v[i]<=m:
                dp[i][j+v[i]] = 1

answer = -1
for j in range(m,-1,-1):
    if dp[n][j] != 0:
        answer = j
        break

print(answer)