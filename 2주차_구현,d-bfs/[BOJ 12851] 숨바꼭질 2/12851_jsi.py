# x-1, x+1, x*2 모두 1임! -> bfs 가능
# 최단 거리 방법 개수는 재방문 가능
# 단, 다시 방문하려면 visited[nx] = visited[x] + 1이어야 함 = 처음 방문한 것보다 오래 걸리면 안 됨
from collections import deque

N, K = map(int, input().split())
visited = [0] * 100001

def bfs(start, dest):
    q = deque([start])
    visited[start] = 0
    time, cnt = 0, 0

    while q:
        x = q.popleft()

        if x == dest:
            time = visited[x]
            cnt += 1
            continue

        for nx in [x-1, x+1, 2*x]:
            if 0 <= nx <= 100000 and (visited[nx] == 0 or visited[nx] == visited[x] + 1):
                visited[nx] = visited[x] + 1
                q.append(nx)
    return [time, cnt]

answer = bfs(N, K)
print(answer[0])
print(answer[1])