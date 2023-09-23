# 25번째 줄 보기
# 되돌아 왔다면 위의 호출에서 해치웠을 것임 굳이 if-else 붙일 필요x
import sys

input = sys.stdin.readline
R, C = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
L, S, word = [], set(), set()
answer = 0

for i in range(R):
    L.append(list(input().rstrip()))
    S = S | set(L[-1])

def dfs(start_x, start_y):
    global answer
    answer = max(answer, len(word))

    for k in range(4):
        nx, ny = start_x + dx[k], start_y + dy[k]
        
        if 0 <= nx < R and 0 <= ny < C and L[nx][ny] not in word:
            word.add(L[nx][ny])
            dfs(nx, ny)
            word.remove(L[nx][ny])

    return

word.add(L[0][0])
dfs(0, 0)
print(answer)
"""
def bfs(start_x, start_y):
    answer = 0
    q = deque()
    q.append((start_x, start_y, 1))
    visited.append(L[start_x][start_y])

    while q:
        x, y, dist = q.popleft()
        is_appended = False

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < R and 0 <= ny < C and L[nx][ny] not in visited:
                q.append((nx, ny, dist + 1))
                visited.append(L[nx][ny])
                is_appended = True
        
        if not is_appended:
            answer = max(answer, dist)
        print(q)
    return answer

print(bfs(0, 0))"""