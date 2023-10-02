'''
1트 => pypy 로 제출 시 정답. python 제출 시 34% 에서 시간초과
'''
# import copy
# import sys
# from collections import deque

# n,m = map(int,input().split())
# _map = []
# for _ in range(n):
#     _map.append(list(map(int,sys.stdin.readline().split())))

# temp = copy.deepcopy(_map)

# dx = [-1,0,1,0]
# dy = [0,-1,0,1]

# def bfs(start_x,start_y):
#     global _map,temp

#     q = deque([(start_x,start_y)])
#     visited = [[False]*m for _ in range(n)]
#     visited[start_x][start_y] = True
    
#     while q:
#         x,y = q.popleft()

#         for i in range(4):
#             nx,ny = x+dx[i], y+dy[i]
#             if not 0<=nx<n or not 0<=ny<m: continue
#             if not visited[nx][ny] and _map[nx][ny] != 0:
#                 visited[nx][ny] = True
#                 q.append((nx,ny))
    
#     for i in range(n):
#         for j in range(m):
#             if _map[i][j] != 0 and not visited[i][j]: return True
#     return False

# def melt():
#     global _map,temp

#     for i in range(n):
#         for j in range(m):
#             if _map[i][j] != 0:
#                 melt_cnt = 0
#                 for k in range(4):
#                     nx,ny = i+dx[k], j+dy[k]
#                     if not 0<=nx<n or not 0<=ny<m: continue
#                     if _map[nx][ny] == 0: melt_cnt += 1
#                 temp[i][j] -= melt_cnt
#                 if temp[i][j] < 0: temp[i][j] = 0
    
#     _map = copy.deepcopy(temp)
                    
# def check():
#     global _map,temp

#     start_x,start_y = -1,-1
#     for i in range(n):
#         for j in range(m):
#             if _map[i][j] != 0:
#                 start_x,start_y = i,j
#                 break
#         if start_x != -1 and start_y != -1: break
    
#     return bfs(start_x,start_y)

# def all_melt():
#     for i in range(n):
#         for j in range(m):
#             if _map[i][j] != 0: return False
#     return True

# year = 0
# flag = False
# while True: 
#     if flag == True:
#         break

#     if all_melt() == True:
#         print(0)
#         exit()

#     melt()
#     flag = check()
#     year += 1

# print(year)


''' 2트 => 시간복잡도 개선
1. copy.deepcopy 사용 X
    - _map 을 복사한 temp 배열을 쓰지 않고, 녹일 빙산들 정보를 리스트로 관리
'''
import sys
from collections import deque

n,m = map(int,input().split())
_map = []
for _ in range(n):
    _map.append(list(map(int,sys.stdin.readline().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(start_x,start_y):
    q = deque([(start_x,start_y)])
    visited = [[False]*m for _ in range(n)]
    visited[start_x][start_y] = True
    
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if not 0<=nx<n or not 0<=ny<m: continue
            if not visited[nx][ny] and _map[nx][ny] != 0:
                visited[nx][ny] = True
                q.append((nx,ny))
    
    for i in range(n):
        for j in range(m):
            if _map[i][j] != 0 and not visited[i][j]: return True
    return False

def melt():
    melt_list = []
    for i in range(n):
        for j in range(m):
            if _map[i][j] != 0:
                melt_cnt = 0
                for k in range(4):
                    nx,ny = i+dx[k], j+dy[k]
                    if not 0<=nx<n or not 0<=ny<m: continue
                    if _map[nx][ny] == 0: melt_cnt += 1
                melt_list.append((i,j,melt_cnt))
    
    for i,j,melt_cnt in melt_list:
        _map[i][j] -= melt_cnt
        if _map[i][j] < 0: _map[i][j] = 0
                    
def check():
    start_x,start_y = -1,-1
    for i in range(n):
        for j in range(m):
            if _map[i][j] != 0:
                start_x,start_y = i,j
                break
        if start_x != -1 and start_y != -1: break
    
    return bfs(start_x,start_y)

def all_melt():
    for i in range(n):
        for j in range(m):
            if _map[i][j] != 0: return False
    return True

year = 0
flag = False
while True: 
    if flag == True:
        break

    if all_melt() == True:
        print(0)
        exit()

    melt()
    flag = check()
    year += 1

print(year)