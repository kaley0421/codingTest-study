# ---------------------------------------------------- 답 참고
# 1. 4차원 visited 배열을 사용해 현재 빨간 구슬과 파란 구슬의 위치 쌍을 저장
# 2. bfs 돌릴 때 move 함수 내 while 문을 통해 '벽이나 구멍을 만날 때까지 구슬이 이동하는 것' 을 구현
# 3. '파란 구슬이 먼저 구멍에 빠져 실패하는 경우', '두 구슬의 위치가 겹친 경우' 에 대한 경우를 고려해 주어야 함
# ----------------------------------------------------
from collections import deque

def move(x,y,dx,dy):
    move_cnt = 0
    while _map[x+dx][y+dy] != '#' and _map[x][y] != 'O':
        x += dx
        y += dy
        move_cnt += 1
    return x,y,move_cnt

def bfs(s_rx,s_ry,s_bx,s_by,_try):
    q = deque([(s_rx,s_ry,s_bx,s_by,_try)])
    visited[s_rx][s_ry][s_bx][s_by] = True

    while q:
        rx,ry,bx,by,_try = q.popleft()

        if _try > 10: break

        for i in range(4):
            nrx,nry,rcnt = move(rx,ry,dx[i],dy[i])
            nbx,nby,bcnt = move(bx,by,dx[i],dy[i])

            if _map[nbx][nby] != 'O':              # 실패 조건이 아니라면
                if _map[nrx][nry] == 'O': 
                    print(_try)
                    exit()
                
                if nrx == nbx and nry == nby:      # 구슬 위치가 겹친 경우, 이동 cnt 가 더 많은 구슬을 한칸 뒤로 이동시킨다. (원래 뒤에 있던 구슬)
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                
                if not visited[nrx][nry][nbx][nby]:       # 이전에 체크하지(방문하지) 않았던 경우라면, 큐에 넣어 탐색을 이어간다.
                    visited[nrx][nry][nbx][nby] = True
                    q.append((nrx,nry,nbx,nby,_try+1))

n,m = map(int,input().split())
_map = []
for _ in range(n):
    _map.append(list(input()))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

rx,ry,bx,by = 0,0,0,0
for i in range(n):
    for j in range(m):
        if _map[i][j] == 'R': rx,ry = i,j
        elif _map[i][j] == 'B': bx,by = i,j

bfs(rx,ry,bx,by,1)

print(-1)