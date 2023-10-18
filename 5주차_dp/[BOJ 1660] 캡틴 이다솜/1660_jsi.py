N = int(input())
L = []
INF = 1e9

now, next = 1, 3
answer = 1
i = 3

while answer <= N:
    L.append(answer)
    answer += next
    now, next = next, next + i
    i += 1

DP = [i for i in range(N + 1)]

for i in range(len(L)):
    DP[L[i]] = 1
    for j in range(L[i] + 1, N + 1):
        DP[j] = min(DP[j], DP[j-L[i]] + DP[L[i]])

print(DP[-1])
# 79 4 35+20+20+4 20+20+20+10+4+4+1 10+10+10+10+10+10+10+4+4+1