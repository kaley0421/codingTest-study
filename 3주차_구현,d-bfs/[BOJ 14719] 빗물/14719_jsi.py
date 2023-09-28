import sys

H, W = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))

answer = 0

for i in range(W):
    if i == 0 or i == W-1:
        answer += min(L[i], max(L)) - L[i]
    else:
        answer += max(L[i], min(max(L[:i]), max(L[i+1:]))) - L[i]

print(answer)