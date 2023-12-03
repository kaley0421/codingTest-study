from itertools import combinations

def check(candi):     # candi 들에 장애물을 놓았을 때 yes/no 여부 확인
    for tx,ty in teachers:
        # tx 행에 대해 student 를 찾을 수 있는지 검사
        for i in range(1,n):
            if (tx,ty-i) in candi: break
            if 0<=ty-i<n:
                if _map[tx][ty-i] == 'S': return False
        for i in range(1,n):
            if (tx,ty+i) in candi: break
            if 0<=ty+i<n:
                if _map[tx][ty+i] == 'S': return False
        # ty 열에 대해 student 를 찾을 수 있는지 검사
        for i in range(1,n):
            if (tx-i,ty) in candi: break
            if 0<=tx-i<n:
                if _map[tx-i][ty] == 'S': return False
        for i in range(1,n):
            if (tx+i,ty) in candi: break
            if 0<=tx+i<n:
                if _map[tx+i][ty] == 'S': return False
    return True

n = int(input())
_map = []
for _ in range(n):
    _map.append(list(input().split()))

_empty = []
teachers = []
for i in range(n):
    for j in range(n):
        if _map[i][j] == 'X':
            _empty.append((i,j))
        if _map[i][j] == 'T':
            teachers.append((i,j))

candis = list(combinations(_empty,3))

for candi in candis:
    if check(candi) == True:
        print("YES")
        exit()
print("NO")