''' 1트 => 제출 시 틀림.. 2차원 dp 열 개수 설정 잘못함.
[ 반례 ]
100 3
7 12
20 30
30 60
입력 시, 정답: 57 / 내 답: 출력 X
---
100 2
7 12
20 30
입력 시, 정답: 67 / 내 답: 출력 X
'''
# c, n = map(int,input().split())
# city = [[0,0]]
# min_cost = 1e9
# for _ in range(n):
#     _c, _g = map(int,input().split())
#     city.append([_c,_g])
#     min_cost = min(min_cost,_c)

# city.sort()

# col = 0
# if c % min_cost == 0: col = c // min_cost
# else: col = c // min_cost + 1

# dp = [[0]*(col+1) for _ in range(n+1)]

# for i in range(1,n+1):
#     base_cost, base_gain = city[i][0], city[i][1]
#     for j in range(1,col+1):
#         if j >= base_cost:
#             dp[i][j] = max(dp[i-1][j-base_cost*(j//base_cost)]+base_gain*(j//base_cost), dp[i-1][j])
#         else:
#             dp[i][j] = dp[i-1][j]

# for j in range(1,col+1):
#     if dp[n][j] >= c:
#         print(j)
#         exit()


''' 2트 => 12% 에서 틀림. 왜 틀렸는지 모르겠.
[ 기존 문제점 ]
100 2
7 12
20 30
입력 시, 정답: 62 / 내 답: 63
=> 원인
    : dp[2][62] 를 고려할 때, dp[1][62](=96) 값을 가져오는 것 vs 20*3 으로 60만큼 cost, 30*3+dp[1][2](=90) 만을 비교.
    : 20*1 + 7*6 으로 62만큼 cost, 30*1 + 12*6 으로 102만큼 가치를 얻는게 더 이득인데, 이 조건을 놓침.
'''
# c, n = map(int,input().split())
# city = [[0,0]]
# min_cost = 1e9
# for _ in range(n):
#     _c, _g = map(int,input().split())
#     city.append([_c,_g])
#     min_cost = min(min_cost,_c)

# city.sort()

# col = 2*c
# dp = [[0]*(col+1) for _ in range(n+1)]

# for i in range(1,n+1):
#     base_cost, base_gain = city[i][0], city[i][1]
#     for j in range(1,col+1):
#         if j >= base_cost:
#             for k in range(1,j//base_cost+1):
#                 dp[i][j] = max(dp[i-1][j-base_cost*k] + base_gain*k, dp[i-1][j], dp[i][j])
#         else:
#             dp[i][j] = dp[i-1][j]


# # print("---- dp")
# # for i in range(0,n+1):
# #     for j in range(0,col+1):
# #         print("j:",j,dp[i][j], end = " ")
# #     print()

# for j in range(1,col+1):
#     if dp[n][j] >= c:
#         print(j)
#         exit()


''' 3트 => 답 참고
'''
c, n = map(int,input().split())
city = [[0,0]]
for _ in range(n):
    _c, _g = map(int,input().split())
    city.append([_c,_g])

dp = [[1e9]*(c+1) for _ in range(n+1)]

for i in range(1,n+1):
    base_cost, base_gain = city[i][0], city[i][1]
    for j in range(1,c+1):
        dp[i][j] = dp[i-1][j]

        k = 0
        while True:
            if j - (k*base_gain) <= 0:
                dp[i][j] = min(dp[i][j], k*base_cost)
                break
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j-k*base_gain]+k*base_cost)
            k += 1

print(dp[n][-1])