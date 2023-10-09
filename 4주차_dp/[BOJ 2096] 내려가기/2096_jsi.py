# 1
# 메모리 초과
# L: 3*N, temp: 1, prev: 3, next:3 -> 약 300,000 * 4 = 1,200,000 bytes = 1.2MB 아닌가??

"""
# 메모리 초과
# L: 3*N, temp: 1, prev: 3, next:3 -> 약 300,000 * 4 = 1,200,000 bytes = 1.2MB 아닌가??
N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

prev, next = [i for i in L[0]], [0] * 3
temp = 0

for i in range(1, N):
    next[0] = max([prev[0], prev[1]]) + L[i][0]
    next[1] = max([prev[0], prev[1], prev[2]]) + L[i][1]
    next[2] = max([prev[1], prev[2]]) + L[i][2]

    prev = [k for k in next]

print(max(prev), end=' ')

prev = L[0]

for i in range(1, N):
    next[0] = min([prev[0], prev[1]]) + L[i][0]
    next[1] = min([prev[0], prev[1], prev[2]]) + L[i][1]
    next[2] = min([prev[1], prev[2]]) + L[i][2]
    
    prev = [k for k in next]

print(min(prev))
"""

# 2
# 경계값 확인하기 N = 1

"""
N = int(input())
L_min, L_max = [0] * 3, [0] * 3
prev_min, prev_max = [0, 0, 0], [0, 0, 0]

for i in range(N):
    L = list(map(int, input().split()))

    if i == 0:
        prev_min, prev_max = [k for k in L], [k for k in L]
        continue

    for idx, j in enumerate([[0, 1], [0, 2], [1, 2]]):
        L_min[idx] = min(prev_min[j[0]:j[1]+1]) + L[idx]
        L_max[idx] = max(prev_max[j[0]:j[1]+1]) + L[idx]

    prev_min, prev_max = [k for k in L_min], [k for k in L_max]

print(max(L_max), min(L_min))
"""
N = int(input())
L_min, L_max = [0] * 3, [0] * 3
next_min, next_max = [0, 0, 0], [0, 0, 0]

for i in range(N):
    L = list(map(int, input().split()))

    if i == 0:
        L_min, L_max = [k for k in L], [k for k in L]
        continue

    for idx, j in enumerate([[0, 1], [0, 2], [1, 2]]):
        next_min[idx] = min(L_min[j[0]:j[1]+1]) + L[idx]
        next_max[idx] = max(L_max[j[0]:j[1]+1]) + L[idx]

    L_min, L_max = [k for k in next_min], [k for k in next_max]

print(max(L_max), min(L_min))