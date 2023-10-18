from collections import deque

N, K = map(int, input().split())

def solution(start):
    q = deque([(start, 0)])
    visited = [False] * 100001
    
    while q:
        x, t = q.popleft()

        if x == K:
            print(t)
            break

        for _ in range(3):
            if 2*x <= min(K*K, 100001) and not visited[2*x]:
                q.append((2*x, t))
                visited[2*x] = True
            if 0 <= x-1 and not visited[x-1]:
                q.append((x-1, t+1))
                visited[x-1] = True
            if x+1 <= K and not visited[x+1]:
                q.append((x+1, t+1))
                visited[x+1] = True
        print(x, q)
solution(N)