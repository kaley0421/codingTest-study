from collections import deque

n,m = map(int,input().split())
_map = []
for _ in range(n):
    _map.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(start_x, start_y):
    q = deque([(start_x,start_y)])
    visited = [[False]*m for _ in range(n)]
    visited[start_x][start_y] = True

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m: continue
            if not visited[nx][ny]:
                # 다음 노드가 1 이면 녹이기 & 다음 노드로는 방문하지 않는다.
                if _map[nx][ny] == 1:
                    _map[nx][ny] = 0
                    visited[nx][ny] = True
                else:
                    q.append((nx,ny))
                    visited[nx][ny] = True

def check_end():
    for i in range(n):
        for j in range(m):
            if _map[i][j] == 1: return False
    return True

def count_cheese():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if _map[i][j] == 1: cnt += 1
    return cnt

time = 0
cheese = 0
while True:
    # 남아 있는 치즈 조각 개수 세기
    cheese = count_cheese()
    # 녹이기
    bfs(0,0)
    time += 1
    # 완료 여부 체크
    if check_end():
        break
    
print(time)
print(cheese)