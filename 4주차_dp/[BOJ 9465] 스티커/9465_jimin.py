''' 1트 => 실패
[ 방식 ]
1. dp 의 행: 스티커 번호 / 열: 해당 스티커를 떼는지 안떼는지 여부
[ 문제점 ]
1. i 번째 스티커를 떼는 경우에 대한 명확한 점화식 안세워짐
2. '예제 1' 에서 30 을 떼는 경우, 바로 위의 50을 떼지 않고 윗 행에서 구할 수 있는 최댓값은 140인데, 이 값을 dp 테이블에서 얻을 수 없음
    << 접근방식이 잘못됐다고 생각되는 이유.
'''
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     sticker = []
#     for _  in range(2):
#         sticker.append(list(map(int,input().split())))

#     dp = [[0]*2 for _ in range(2*n)]
#     dp[0][0], dp[0][1] = 0, sticker[0][0]
#     dp[1][0] = dp[0][1]
#     dp[1][1] = sticker[0][1]

#     for i in range(2,2*n):                # i 번째 스티커
#         # i 번째 스티커를 안떼는 경우
#         dp[i][0] = max(dp[i-1][0],dp[i-1][1])
#         # i 번째 스티커를 떼는 경우
#         dp[i][1] = max(dp[i-2][0],dp[i-1][0])+sticker[i//n][i%n]
        
#     print(max(dp[2*n-1][0],dp[2*n-1][1]))


''' 2트 => 답 참고
1. 1트에서는 1행의 왼->오 로 이동하며 탐색 후 2행의 왼->오 로 이동하며 탐색하며 dp 테이블을 갱신 
    >> 왼->오 로 이동하며 i열에 대해 dp 테이블을 갱신하는 방식 으로 수정
2. dp 테이블에 해당 스티커 위치에서 얻을 수 있는 최대 이익 저장
'''
t = int(input())
for _ in range(t):
    n = int(input())
    dp = []
    for _  in range(2):
        dp.append(list(map(int,input().split())))

    if n > 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]

    for i in range(2,n):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])
    
    print(max(dp[0][n-1],dp[1][n-1]))