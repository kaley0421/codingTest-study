# ---------------------------------------------------- 답 참고.
# 1. 맵의 안/밖을 오가야 하는 경우에는 맵을 상하좌우로 1씩 늘려주는게 좋다?
# 2. 1번 죄수, 2번 죄수, 상근이(외부에서 들어오는 제3자) 가 돌아다니는 것을 고려하기 위해 bfs 를 3번 돌려 최소값을 찾는다.
# 3. '문' 을 카운트 하는 경우, 한 명이 열면 다른 두명은 안 열어도 되므로 -2 해준다.
# 4. bfs 돌릴 때 지나갈 수 있는 길인 경우에는 우선적으로 그 길로 갈 수 있게 하기 위해 appendleft 함수를 사용한다.
# => 왜 다익스트라 문제로 구분되어 있는지 모르겠다.
# => '0-1 너비 우선 탐색' 에 대해서 공부해볼것.
# => 완벽히 이해는 못함. 나중에 다시 풀어보자...!
# [ 참고 링크: https://vicente-blog.com/blog/31/ ]
# ----------------------------------------------------
import sys
from collections import deque

input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(start_y, start_x):
    q = deque()
    cnt = [[-1] * (w + 2) for _ in range(h + 2)]

    q.append([start_y, start_x])
    cnt[start_y][start_x] = 0

    while q:
        cur_y, cur_x = q.popleft()

        for i in range(4):
            next_y, next_x = cur_y + dy[i], cur_x + dx[i]

            if 0 <= next_y < h + 2 and 0 <= next_x < w + 2:
                if cnt[next_y][next_x] == -1:
                    if _map[next_y][next_x] == '.':
                        q.appendleft([next_y, next_x])
                        cnt[next_y][next_x] = cnt[cur_y][cur_x]
                    elif _map[next_y][next_x] == '#':
                        q.append([next_y, next_x])
                        cnt[next_y][next_x] = cnt[cur_y][cur_x] + 1
    return cnt

t = int(input().strip())

for _ in range(t):
    h, w = map(int, input().split())
    _map = [['.'] * (w + 2)]
    for i in range(h):
        _map.append(list('.' + input().strip() + '.'))
    _map.append(['.'] * (w + 2))
    start = []

    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if _map[i][j] == '$':
                start.append([i, j])
                _map[i][j] = '.'

    cnt1 = bfs(start[0][0], start[0][1])
    cnt2 = bfs(start[1][0], start[1][1])
    cnt3 = bfs(0, 0)

    ans = float('inf')
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if cnt1[i][j] != -1 and cnt2[i][j] != -1 and cnt3[i][j] != -1:
                if _map[i][j] == '.':
                    ans = min(ans, cnt1[i][j] + cnt2[i][j] + cnt3[i][j])
                elif _map[i][j] == '#':
                    ans = min(ans, cnt1[i][j] + cnt2[i][j] + cnt3[i][j] - 2)
    print(ans)