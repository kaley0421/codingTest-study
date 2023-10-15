"""
INF = 1e9
LIMIT = 0

C, N = map(int, input().split())
cost, customer = [0], [0]

for i in range(N):
    a, b = map(int, input().split())
    LIMIT = max(LIMIT, (C // b + 1) * b + 1)
    
    cost.append(a)
    customer.append(b)

DP = [INF] * LIMIT
DP[0] = 0

for i in range(1, N + 1):
    for j in range(customer[i], LIMIT, customer[i]):
        DP[j] = min(DP[j], DP[j - customer[i]] + cost[i])
        
print(min(DP[C:]))
"""

C, N = map(int, input().split())
cost, customer = [0], [0]

LIMIT = C + 100
INF = 1e9

for i in range(N):
    a, b = map(int, input().split())
    
    cost.append(a)
    customer.append(b)

DP = [INF] * LIMIT
DP[0] = 0

for i in range(1, N + 1):
    for j in range(customer[i], LIMIT):
        DP[j] = min(DP[j], DP[j - customer[i]] + cost[i])
        
print(min(DP[C:]))
"""
DP[i] = 고객이 i일 때까지 최소 비용
1 2 3 4 5 6 7 8 9 10 11 12
        3         6
1 2 3 4 3 4 5 6 7 6 7 8
"""