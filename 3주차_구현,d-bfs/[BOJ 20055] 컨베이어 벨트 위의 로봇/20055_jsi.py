import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
A = deque(list(map(int, sys.stdin.readline().rstrip().split())))
R = deque([False] * (2*N))

cnt = 0
q = deque()

while A.count(0) < K:
    A.appendleft(A.pop())
    R.appendleft(R.pop())
    R[N-1] = False
    
    for cur in range(N-2, -1, -1):
        next = cur + 1

        if R[cur] == True and R[next] == False and A[next] > 0:
            R[next] = R[cur]
            R[cur] = False
            A[next] -= 1
    R[N-1] = False
    
    if 0 < A[0]:
        R[0] = True
        A[0] -= 1

    cnt += 1

print(cnt)