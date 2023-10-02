''' 1트 => 30% 에서 틀림
[ 틀린 이유 ]
- 공격 대상을 찾을 때 '가장 가까운 적 찾기' 로직 틀림 => bfs 로 바꿔볼 것
'''
# import copy
# from itertools import combinations

# n,m,d = map(int,input().split())
# ori_map = []
# for _ in range(n):
#     ori_map.append(list(map(int,input().split())))

# arrows = list(combinations([i for i in range(m)],3))

# def check_end():
#     for i in range(n):
#         for j in range(m):
#             if _map[i][j] == 1: return False
#     return True

# def attack(arrow):
#     dying = []
#     for attacker in arrow:
#         attacked = False
#         for i in range(n-1,-1,-1):
#             for j in range(m):
#                 if _map[i][j] == 1 and abs(n-i) + abs(attacker-j) <= d:
#                     if (i,j) not in dying: 
#                         dying.append((i,j))
#                     attacked = True
#                     break
#             if attacked == True: break
    
#     for i,j in dying:
#         _map[i][j] = 0
#     return len(dying)

# def move():
#     for i in range(n-1,0,-1):
#         for j in range(m):
#             _map[i][j] = _map[i-1][j]
#     for j in range(m):
#         _map[0][j] = 0

# _map = []
# answer = 0
# for arrow in arrows:
#     _map = copy.deepcopy(ori_map)

#     died = 0
#     while check_end() == False:
#         died += attack(arrow)
#         move()

#     answer = max(answer,died)

# print(answer)


''' 2트
1. bfs + heapq 사용해서 공격할 적 선정
'''
import copy
import heapq
from itertools import combinations

n,m,d = map(int,input().split())
ori_map = []
for _ in range(n):
    ori_map.append(list(map(int,input().split())))

arrows = list(combinations([i for i in range(m)],3))

dx = [-1,0,1]
dy = [0,-1,0]

def check_end():
    for i in range(n):
        for j in range(m):
            if _map[i][j] == 1: return False
    return True

def attack(arrow):
    dying = []
    for attacker in arrow:
        attacked = False

        # 공격 대상 찾기 -> dying 에 추가
        q = []
        visited = [[False]*m for _ in range(n)]
        heapq.heappush(q,(0,attacker,n))
        attacked = False
        while q:
            step,x,y = heapq.heappop(q)

            for i in range(3):
                nx,ny = x+dx[i], y+dy[i]

                if not 0<=nx<m or not 0<=ny<n: continue
                if step + 1 > d: continue

                if not visited[ny][nx]:
                    if _map[ny][nx] == 1:
                        if (ny,nx) not in dying: dying.append((ny,nx))
                        attacked = True
                        break
                    heapq.heappush(q,(step+1,nx,ny))
                    visited[ny][nx] = True

            if attacked == True: break
            
    for i,j in dying:
        _map[i][j] = 0
    return len(dying)

def move():
    for i in range(n-1,0,-1):
        for j in range(m):
            _map[i][j] = _map[i-1][j]
    for j in range(m):
        _map[0][j] = 0

_map = []
answer = 0
for arrow in arrows:
    _map = copy.deepcopy(ori_map)

    died = 0
    while check_end() == False:
        died += attack(arrow)
        move()

    answer = max(answer,died)

print(answer)