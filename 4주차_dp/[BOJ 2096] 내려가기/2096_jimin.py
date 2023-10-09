''' 1트 => 메모리 초과. 원인 파악 불가.
'''
# import copy

# n = int(input())
# _map = []
# for _ in range(n):
#     _map.append(list(map(int,input().split())))

# max_dp = copy.deepcopy(_map[0])
# min_dp = copy.deepcopy(_map[0])

# next_max = [0]*3
# next_min = [0]*3

# for i in range(1,n):
#     for j in range(3):
#         max_temp, min_temp = 0, 1e9
#         for direct in range(-1,2):
#             if 0 <= j+direct < 3:
#                 max_temp = max(max_temp, max_dp[j+direct] + _map[i][j])
#                 min_temp = min(min_temp, min_dp[j+direct] + _map[i][j])
#         next_max[j] = max_temp
#         next_min[j] = min_temp
    
#     for i in range(3):
#         max_dp[i], min_dp[i] = next_max[i], next_min[i]

# print(max(max_dp), min(min_dp))


''' 2트 => 답 참고
'''
import sys

input = sys.stdin.readline

n = int(input())

max_dp = [0] * 3
min_dp = [0] * 3

next_max = [0] * 3
next_min = [0] * 3

for i in range(n):
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            next_max[j] = a + max(max_dp[j], max_dp[j + 1])
            next_min[j] = a + min(min_dp[j], min_dp[j + 1])
        elif j == 1:
            next_max[j] = b + max(max_dp[j - 1], max_dp[j], max_dp[j + 1])
            next_min[j] = b + min(min_dp[j - 1], min_dp[j], min_dp[j + 1])
        else:
            next_max[j] = c + max(max_dp[j], max_dp[j - 1])
            next_min[j] = c + min(min_dp[j], min_dp[j - 1])

    for j in range(3):
        max_dp[j] = next_max[j]
        min_dp[j] = next_min[j]

print(max(max_dp), min(min_dp))


''' 3트 => 1트 수정
1. _map 입력을 수정
    : _map 을 반복적으로 새로운 리스트로 덮어씌우면, 새 주소가 할당되고 새로운 메모리가 할당되는건 맞지만, GC 가 사용하지 않는 기존 메모리를 제거해줌
    : _map 을 2차원 리스트로 한번에 초기 할당해 놓는 것보다 메모리 효율 굳
'''
import sys

n = int(input())

max_dp = [0]*3
min_dp = [0]*3

next_max = [0]*3
next_min = [0]*3

for i in range(n):
    _map = list(map(int,sys.stdin.readline().split()))

    for j in range(3):
        max_temp, min_temp = 0, 1e9
        for direct in range(-1,2):
            if 0 <= j+direct < 3:
                max_temp = max(max_temp, max_dp[j+direct] + _map[j])
                min_temp = min(min_temp, min_dp[j+direct] + _map[j])
        next_max[j] = max_temp
        next_min[j] = min_temp
    
    for i in range(3):
        max_dp[i], min_dp[i] = next_max[i], next_min[i]

print(max(max_dp), min(min_dp))