# ---------------------------------------------------- 1트 => 63% 에서 시간초과
# r,c = map(int,input().split())
# _map = []
# for _ in range(r):
#     _map.append(list(input()))

# dx = [-1,0,1,0]
# dy = [0,-1,0,1]

# visited_alpha = dict()

# def dfs(x,y,step):
#     global answer
#     answer = max(answer,step)

#     visited_alpha[_map[x][y]] = 1

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if nx<0 or nx>=r or ny<0 or ny>=c: continue

#         if _map[nx][ny] not in visited_alpha:
#             visited_alpha[_map[nx][ny]] = 1
#             dfs(nx,ny,step+1)
#             del(visited_alpha[_map[nx][ny]])

# answer = 0
# dfs(0,0,1)
# print(answer)


# ---------------------------------------------------- 2트 => 방문한 알파켓 마킹방식 변경
r,c = map(int,input().split())
_map = []
for _ in range(r):
    _map.append(list(input()))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

visited_alpha = [0] * 26

def dfs(x,y,step):
    global answer
    answer = max(answer,step)

    visited_alpha[ord(_map[x][y])-ord('A')] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or nx>=r or ny<0 or ny>=c: continue

        if visited_alpha[ord(_map[nx][ny])-ord('A')] == 0:
            visited_alpha[ord(_map[nx][ny])-ord('A')] = 1
            dfs(nx,ny,step+1)
            visited_alpha[ord(_map[nx][ny])-ord('A')] = 0

answer = 0
dfs(0,0,1)
print(answer)