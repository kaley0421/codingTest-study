# BOJ_1715
# 중복해서 더하는 값은 최소여야 함 > 최소힙 사용

import heapq

N = int(input())
L = []
answer = 0

for _ in range(N):
    heapq.heappush(L, int(input()))

if N == 1:
    answer = 0
else:
    while len(L) > 1:
        a, b = heapq.heappop(L), heapq.heappop(L)
        answer += a + b
        heapq.heappush(L,  a + b)

print(answer)
