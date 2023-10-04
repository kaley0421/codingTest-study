N = int(input())

x, y, z = 1, 1, 1
answer = 3

for i in range(1, N):
    answer = (3*x + 2*y + 2*z) % 9901
    x, y, z = x+y+z, x+z, x+y

print(answer)

# 1차원 배열으로 해도 메모리 초과
"""
N = int(input())
DP = [1] * (N+1)

x, y, z = 1, 1, 1
DP[1] = 3

for i in range(2, N+1):
    DP[i] = 3*x + 2*y + 2*z
    x, y, z = x+y+z, x+z, x+y

print(DP[N])
"""

# 3 * (N+1) 배열이라서 그런지 메모리 초과
"""
N = int(input())
DP = [[1] * 3 for _ in range(N+1)]

DP[1] = [1, 1, 1]

for i in range(2, N+1):
    DP[i][0] = DP[i-1][0] + DP[i-1][1] + DP[i-1][2]
    DP[i][1] = DP[i-1][0] + DP[i-1][2]
    DP[i][2] = DP[i-1][0] + DP[i-1][1]
print(sum(DP[-1]))
"""