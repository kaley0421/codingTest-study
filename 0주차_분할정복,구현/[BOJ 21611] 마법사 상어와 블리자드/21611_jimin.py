'''
- 같은 번호의 구슬이 연속한 칸에 존재 => '연속하는 구슬'

[ 블리자드 마법 ]
1. d 방향으로 거리가 s 이하인 칸에 있는 구슬들 파괴
2. 구슬 이동
    - 어떤 칸 A 보다 번호가 하나 작은 칸이 빈 칸이면, A 의 구슬이 이동
3. 구슬 폭발
    - '4개 이상 연속하는 구슬' 이 있을 때 그 구슬들이 폭발
4. 구슬 이동 >> 다시 폭발 >> 이동..
    - 더이상 폭발할 구슬이 없을 때까지 반복
5. 구슬 변화
    - 연속하는 구슬들은 하나의 그룹
    - 하나의 그룹 >> 구슬 A,B 로 변화
        A: 그룹에 속한 구슬의 개수
        B: 그룹을 이루고 있는 구슬들의 번호
    - 변화한 구슬들은 다시 원래 그룹의 순서대로 칸에 들어감
    - 다 들어가지 못하는 경우, 구슬 소멸

- answer: 1*폭발한 1번구슬 개수 + 2*폭발한 2번구슬 개수 + 3*폭발한 3번구슬 개수
'''

''' 1트 => 63% 시간초과
'''
# import sys

# def destroy(d,s):
#     d -= 1
#     shark_x, shark_y = n//2, n//2
#     for i in range(1,s+1):
#         _map[shark_x+dx[d]*i][shark_y+dy[d]*i] = 0

# def map_num():
#     x, y = n//2, n//2
#     cnt = 0
#     num = 0
#     for _ in range(n//2):     
#         if x == 0 and y == 0: break
#         else:
#             y -= 1
#             cnt += 2
#             num += 1
#             num_pos[num] = (x,y)
#             for direction in range(4):
#                 if direction == 0:
#                     for _ in range(cnt-1):
#                         x += cx[direction]
#                         y += cy[direction]
#                         num += 1
#                         num_pos[num] = (x,y)
#                 else:
#                     for _ in range(cnt):
#                         x += cx[direction]
#                         y += cy[direction]
#                         num += 1
#                         num_pos[num] = (x,y)

# def move():
#     for i in range(1,n*n):
#         x,y = num_pos[i]
#         if _map[x][y] == 0:
#             for j in range(i+1,n*n):
#                 nx,ny = num_pos[j]
#                 if _map[nx][ny] != 0:             
#                     _map[x][y] = _map[nx][ny]
#                     _map[nx][ny] = 0
#                     break

# def get_pop_list():
#     result = set()
#     for i in range(1,n*n):
#         x,y = num_pos[i]
#         if _map[x][y] == 0: break
#         temp = [(x,y)]
#         for j in range(i+1,n*n):
#             nx,ny = num_pos[j]
#             if _map[nx][ny] != _map[x][y]: break
#             temp.append((nx,ny))
#         if len(temp) >= 4:
#             for t in temp: result.add(t)
#     return result

# def change():
#     marbles = []
#     visited = [False] * (n*n)
#     for i in range(1,n*n):
#         x,y = num_pos[i]
#         if _map[x][y] == 0: break
#         if visited[i] == True: continue
#         visited[i] = True
#         cnt, num = 1, _map[x][y]
#         for j in range(i+1, n*n):
#             nx,ny = num_pos[j]
#             if _map[nx][ny] != _map[x][y]: break
#             cnt += 1
#             visited[j] = True
#         marbles.append(cnt)
#         marbles.append(num)
#     return marbles
    
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# cx = [1,0,-1,0]
# cy = [0,1,0,-1]

# num_pos = dict()
# popped = dict()
# popped[1] = 0
# popped[2] = 0
# popped[3] = 0

# n,m = map(int,sys.stdin.readline().split())
# _map = []
# for _ in range(n):
#     _map.append(list(map(int,sys.stdin.readline().split())))

# map_num()

# for _ in range(m):
#     d,s = map(int,sys.stdin.readline().split())

#     destroy(d,s)

#     move()
  
#     while True:
#         pop_list = list(get_pop_list())
#         if len(pop_list) == 0: break
#         # pop_list 들 폭발
#         for px,py in pop_list:
#             popped[_map[px][py]] += 1
#             _map[px][py] = 0
#         # 구슬 이동
#         move()

#     new_marbles = change()
#     idx = 1
#     for marble in new_marbles:
#         if idx >= n*n: break
#         x,y = num_pos[idx]
#         _map[x][y] = marble
#         idx += 1
   
# print(1*popped[1]+2*popped[2]+3*popped[3])



''' 2트 => 답 참고.
- 1트와 접근방식은 똑같
    1. coord 딕셔너리를 사용해서 2차원 배열 정보를 coord[지도 상 n번째 칸] = (x,y) 로 관리
        : 2차원 지도의 순회 방향(?) 을 관리하는데 편하다.
        : init() 함수로 딕셔너리를 초기화한다. (1트에서의 map_num() 함수와 동일)

[ 1트와의 차이점 ]
1. move() 함수
    - 1트의 구현: 모든 i 번째 칸들에 대해서, i 번째 이후 j 번째 칸이 0 이 아닌 곳이 나올 때까지 탐색.
                더이상 구슬이 없는 i 번째 칸들에 대해서는 계속 j가 n*n 이 될때까지 탐색해서 비효율적.
    - 2트의 구현: cur(현재 칸) & target(탐색중인 칸) 변수 두개를 두고 관리.
                target 은 cur 번째 칸 이후 칸들을 탐색하며 0 이 아닌 곳을 찾는다.
                target 이나 cur 이 n*n 에 도달했다면, 탐색 종료.
                ex. cur = 39, target = 49 인 경우
                    -> cur 이후 칸들은 모두 빈 칸이라는 것을 의미.
                    -> 마지막 for 문으로 뒤에 남은 칸들은 한번에 0 으로 채워준다.
'''
import sys

def init():
    x, y = n//2, n//2
    cnt = 0
    num = 0
    cx = [1,0,-1,0]
    cy = [0,1,0,-1]
    for _ in range(n//2):     
        if x == 0 and y == 0: break
        else:
            y -= 1
            cnt += 2
            num += 1
            coord[num] = (x,y)
            for direction in range(4):
                if direction == 0:
                    for _ in range(cnt-1):
                        x += cx[direction]
                        y += cy[direction]
                        num += 1
                        coord[num] = (x,y)
                else:
                    for _ in range(cnt):
                        x += cx[direction]
                        y += cy[direction]
                        num += 1
                        coord[num] = (x,y)

def destroy(d,s):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    d -= 1
    shark_x, shark_y = n//2, n//2
    for i in range(1,s+1):
        _map[shark_x+dx[d]*i][shark_y+dy[d]*i] = 0

def move():
    cur = 1
    target = cur
    while cur < n*n and target < n*n:
        cx,cy = coord[cur]
        nx,ny = coord[target]
        while target < n*n-1 and _map[nx][ny] == 0:
            target += 1
            nx,ny = coord[target]
        _map[cx][cy] = _map[nx][ny]    # (nx,ny) 가 0이 아닌 곳을 찾아서 해당 구슬을 (cx,cy) 로 옮긴다.
        cur += 1
        target += 1
    
    for i in range(n*n - (target-cur), n*n):    # 뒤에 남은 칸들은 0으로 채워준다.
        cx,cy = coord[i]
        _map[cx][cy] = 0

# def move():                            <<<< 1트
#     for i in range(1,n*n):
#         x,y = coord[i]
#         if _map[x][y] == 0:
#             for j in range(i+1,n*n):
#                 nx,ny = coord[j]
#                 if _map[nx][ny] != 0:             
#                     _map[x][y] = _map[nx][ny]
#                     _map[nx][ny] = 0
#                     break

def get_pop_list():
    result = set()
    for i in range(1,n*n):
        x,y = coord[i]
        if _map[x][y] == 0: break
        temp = [(x,y)]
        for j in range(i+1,n*n):
            nx,ny = coord[j]
            if _map[nx][ny] != _map[x][y]: break
            temp.append((nx,ny))
        if len(temp) >= 4:
            for t in temp: result.add(t)
    return result

def change():
    marbles = []
    visited = [False] * (n*n)
    for i in range(1,n*n):
        x,y = coord[i]
        if _map[x][y] == 0: break
        if visited[i] == True: continue
        visited[i] = True
        cnt, num = 1, _map[x][y]
        for j in range(i+1, n*n):
            nx,ny = coord[j]
            if _map[nx][ny] != _map[x][y]: break
            cnt += 1
            visited[j] = True
        marbles.append(cnt)
        marbles.append(num)
    return marbles

n,m = map(int,sys.stdin.readline().split())
_map = []
for _ in range(n):
    _map.append(list(map(int, sys.stdin.readline().split())))

score = 0

popped = dict()
popped[1] = 0
popped[2] = 0
popped[3] = 0

coord = dict()
init()

for _ in range(m):
    d,s = map(int, sys.stdin.readline().split())
    
    destroy(d,s)

    move()

    # 구슬 폭발
    while True:
        pop_list = list(get_pop_list())
        if len(pop_list) == 0: break
        # pop_list 들 폭발
        for px,py in pop_list:
            popped[_map[px][py]] += 1
            _map[px][py] = 0
        # 구슬 이동
        move()
    score = 1*popped[1]+2*popped[2]+3*popped[3]

    # 구슬 변화
    new_marbles = change()
    idx = 1
    for marble in new_marbles:
        if idx >= n*n: break
        x,y = coord[idx]
        _map[x][y] = marble
        idx += 1

print(score)