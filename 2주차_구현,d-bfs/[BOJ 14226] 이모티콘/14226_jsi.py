# 모든 연산은 1초 -> bfs/dfs 가능
# 클립보드의 이모지 수는 화면의 이모지 수보다 클 수 없음 (화면을 복사하므로) > clipboad <= screen
# 화면의 이모지 수가 1000이 넘으면 삭제만 하면 됨 -> 1000이 넘으면 복사할 필요가 없으므로 clipboard <= S

from collections import deque

S = int(input())
visited = [[] for _ in range(2001)]

def bfs(clipboard, screen):
    # 클립보드, 화면
    q = deque([(clipboard, screen, 0)])
    visited[clipboard].append(screen)
    
    while q:
        clipboard, screen, time = q.popleft()

        if screen == S:
            return time

        # 복사, 삭제
        if screen != 0:
            if screen not in visited[screen]:
                q.append((screen, screen, time + 1))
                visited[screen].append(screen)
            if 1 < screen and screen - 1 not in visited[clipboard] :
                q.append((clipboard, screen - 1, time + 1))
                visited[clipboard].append(screen - 1)
        # 붙여넣기
        if clipboard != 0:
            if screen <= S and screen + clipboard not in visited[clipboard]:
                q.append((clipboard, screen + clipboard, time + 1))
                visited[clipboard].append(screen + clipboard)
    return -1

print(bfs(0, 1))