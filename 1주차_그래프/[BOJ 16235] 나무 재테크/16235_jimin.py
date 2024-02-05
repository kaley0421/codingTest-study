''' 1트 => dictionary 사용. 시간초과
'''
# import sys

# n,m,total_years = map(int,sys.stdin.readline().split())
# A = []
# for _ in range(n):
#     A.append(list(map(int,sys.stdin.readline().split())))

# _map = [[5]*n for _ in range(n)]
# dx = [-1,-1,-1,0,0,1,1,1]
# dy = [-1,0,1,-1,1,-1,0,1]

# trees = dict()
# dead = dict()
# for _ in range(m):
#     x,y,age = map(int,sys.stdin.readline().split())
#     if (x-1, y-1) in trees:
#         trees[(x-1, y-1)].append(age)
#     else:
#         trees[(x-1, y-1)] = [age]

# years = 0
# while years < total_years:
#     # 봄
#     deleting = []
#     for (i,j) in trees.keys():
#         trees[(i,j)].sort()           # trees[(i,j)] -> (i,j) 에 심어져 있는 나무들의 나이 배열
#         for k in range(len(trees[(i,j)])):   # 해당 칸에 심어져 있는 나무들 순회
#             # 자신의 나이만큼 양분 섭취 & 나이 1 증가
#             if _map[i][j] >= trees[(i,j)][k]:
#                 _map[i][j] -= trees[(i,j)][k]
#                 trees[(i,j)][k] += 1
#             # 자신의 나이만큼 먹지 못하면 -> 죽음 (+ 같은 칸에 존재하는 더 나이 많은 나무들도 모두 죽음)
#             else:
#                 if k == 0:    # 해당 칸에 있는 나무들 모두 죽음
#                     dead[(i,j)] = []
#                     for dead_age in trees[(i,j)]:
#                         dead[(i,j)].append(dead_age)
#                     deleting.append((i,j))
#                     break
#                 if (i,j) in dead:
#                     for dead_age in trees[(i,j)][k:]:
#                         dead[(i,j)].append(dead_age)
#                 else:
#                     dead[(i,j)] = []
#                     for dead_age in trees[(i,j)][k:]:
#                         dead[(i,j)].append(dead_age)
#                 trees[(i,j)] = trees[(i,j)][:k]
#                 if len(trees[(i,j)]) == 0:
#                     deleting.append((i,j))
#                 break
#     for (x,y) in deleting:
#         if (x,y) in trees:
#             del(trees[(x,y)])
                
#     # 여름
#     # 죽은 나무의 나이 // 2 가 나무가 있던 칸의 양분으로 추가됨
#     for (i,j) in dead.keys():
#         for dead_age in dead[(i,j)]:
#             _map[i][j] += dead_age // 2          
#     dead.clear()

#     # 가을
#     # 나이가 5의 배수인 나무들 번식 : 인접한 8개의 칸에 나이 1 인 나무 생성
#     adding = []
#     for (i,j) in trees.keys():
#         ages = trees[(i,j)]
#         for age in ages:
#             if age % 5 == 0:
#                 for k in range(8):
#                     if i+dx[k] < 0 or i+dx[k] >= n or j+dy[k] < 0 or j+dy[k] >= n: 
#                         continue
#                     adding.append((i+dx[k], j+dy[k]))
#     for (x,y) in adding:
#         if (x,y) in trees:
#             trees[(x,y)].append(1)
#         else:
#             trees[(x,y)] = [1]

#     # 겨울
#     # 각 땅에 A[r][c] 만큼의 양분 추가
#     for i in range(n):
#         for j in range(n):
#             _map[i][j] += A[i][j]

#     years += 1
    
# answer = 0
# for (i,j) in trees.keys():
#     answer += len(trees[(i,j)])
# print(answer)



''' 2트 => deque 사용
1. 입력으로 주어지는 나무 위치는 모두 다름 
    -> 새로 생성되는 나무들은 deque.appendleft() 함수로 큐의 앞쪽에 넣어주면 됨.
    -> 정렬 필요 없이 '나이 어린 나무부터 양분을 섭취한다' 는 조건 만족 가능.
'''
import sys
from collections import deque

n,m,total_years = map(int,sys.stdin.readline().split())
A = []
for _ in range(n):
    A.append(list(map(int,sys.stdin.readline().split())))

_map = [[5]*n for _ in range(n)]
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

trees = [[deque() for _ in range(n)] for _ in range(n)]
dead = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,age = map(int,sys.stdin.readline().split())
    trees[x-1][y-1].append(age)

years = 0
while years < total_years:
    # 봄
    for i in range(n):
        for j in range(n):
            _len = len(trees[i][j])
            for k in range(_len):
                # 자신의 나이만큼 양분 섭취 & 나이 1 증가
                if _map[i][j] >= trees[i][j][k]:
                    _map[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                # 자신의 나이만큼 먹지 못하면 -> 죽음 (+ 같은 칸에 존재하는 더 나이 많은 나무들도 모두 죽음)
                else:
                    for _ in range(k, _len):
                        dead[i][j].append(trees[i][j].pop()) 
                    break

    # 여름
    # 죽은 나무의 나이 // 2 가 나무가 있던 칸의 양분으로 추가됨
    for i in range(n):
        for j in range(n):
            while dead[i][j]:
                _map[i][j] += dead[i][j].pop() // 2

    # 가을
    # 나이가 5의 배수인 나무들 번식 : 인접한 8개의 칸에 나이 1 인 나무 생성
    for i in range(n):
        for j in range(n):
            for k in range(len(trees[i][j])):     # (i,j) 에 존재하는 나무들 순회
                if trees[i][j][k] % 5 == 0:
                    for d in range(8):
                        nx,ny = i+dx[d], j+dy[d]
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        # 새로 생성된 나무들 앞으로 삽입
                        trees[nx][ny].appendleft(1)

    # 겨울
    # 각 땅에 A[r][c] 만큼의 양분 추가
    for i in range(n):
        for j in range(n):
            _map[i][j] += A[i][j]

    years += 1
   

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])
print(answer)