# DP[x] = x번을 포함한 x번까지 증가하는 수열 최대 합

N = int(input())
A = list(map(int, input().split()))
DP = [i for i in A]

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            DP[i] = max(DP[i], DP[j] + A[i])
print(DP)
print(max(DP))