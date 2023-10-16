N = int(input())
M = int(input())
L = [0] + [int(input()) for _ in range(M)]
DP = [[0] * 3 for _ in range(N + 1)]

DP[1] = [0, 1, 1]

for x in range(2, N + 1):
    if x in L:
        DP[x] = [0, DP[x-1][0] + DP[x-1][1], 0]
        continue
    
    DP[x][0] = DP[x-1][2]
    DP[x][1] = DP[x-1][0] + DP[x-1][1]
    DP[x][2] = DP[x-1][0] + DP[x-1][1]

    if x-1 in L or x-1 == 0:
        DP[x][0] = 0
    if x+1 in L or x+1 == N + 1:
        DP[x][2] = 0
    
print(sum(DP[-1]))
"""

1   2   3   4   5   6   7   8   9
            4           7
1   2   3       5   6       8   9
2   1   3       5   6       8   9
1   3   2       5   6       8   9


1   2   3   4
1   3   2   4
1   2   4   3
2   1   3   4

DP
0   0
1   
1
DP[x][0] = DP[x-1][2]
DP[x][1] = DP[x-1][0] + DP[x-1][1]
DP[x][2] = DP[x-1][0] + DP[x-1][1]

왼, 가, 오에 앉을 수 있음
x가 왼쪽이랑 바꾸면 x-1, x, x+1이 고정됨
x가 오른쪽이랑 바꾸면 x, x+1이 고정됨

x-1이 왼쪽이랑 바꿨다면 x는 가만히 or 오른쪽
x-1이 가만히 있는다면 x는 가만히 or 오른쪽
x-1이 오른쪽이랑 바꾼다면 x는 왼쪽
DP[x] = DP[x-1][0] * 2 + DP[x-1][1] * 2 + DP[x-1][2]


왼쪽에 앉으면 원래 왼쪽에 있는 애랑 바꿔야 함
    왼쪽 애가 자리 바꿨으면 못 바꿈
오른쪽에 앉으면 원래 오른쪽에 있는 애랑 바꿔야 함

DP[x] = DP[x-1], 
"""