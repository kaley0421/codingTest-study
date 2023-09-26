'''
1. bfs 알고리즘을 떠올리는게 핵심
2. (현재 화면의 이모티콘 개수, 현재 클립보드의 이모티콘 개수) 조합을 탐색해 나간다.
'''
from collections import deque

s = int(input())

visited = [[-1] * (2*s) for _ in range(2*s)]
visited[1][0] = 0

q = deque([(1,0)])
while q:
    screen, board = q.popleft()
    cur_time = visited[screen][board]

    if screen == s:
        print(cur_time)
        exit()

    # 화면에 있는 이모티콘을 복사해서 클립보드에 저장
    if visited[screen][screen] == -1:
        visited[screen][screen] = cur_time + 1
        q.append((screen,screen))

    if board > 0:
        # 클립보드의 이모티콘을 화면에 붙여넣기
        if screen+board < 2*s and visited[screen+board][board] == -1:
            visited[screen+board][board] = cur_time + 1
            q.append((screen+board,board))

    # 화면에 있는 이모지 중 하나 삭제
    if screen-1 >= 0 and visited[screen-1][board] == -1:
        visited[screen-1][board] = cur_time + 1
        q.append((screen-1,board))