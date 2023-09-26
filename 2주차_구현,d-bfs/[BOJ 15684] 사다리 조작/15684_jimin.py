# 답 참고해서 풀었으나 시간초과.. 다시 풀어볼 것.

import sys

n,m,h = map(int,sys.stdin.readline().split())
_map = [[0]*n for _ in range(h)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    _map[a-1][b-1] = 1

def check():
    for i in range(n):
        temp = i
        for j in range(h):
            if _map[j][temp]:
                temp += 1
            elif temp > 0 and _map[j][temp-1]:
                temp -= 1
        if temp != i:
            return False
    return True

def dfs(x,y,step):
    global answer
    
    if answer <= step:
        return
    if check():
        answer = min(answer,step)
        return
    if step == 3:
        return
    
    for i in range(x,h):
        if i == x:
            k = y
        else:
            k = 0

        for j in range(k,n-1):
            if _map[i][j] == 0:
                _map[i][j] = 1
                dfs(i,j+2,step+1)
                _map[i][j] = 0

answer = 4
dfs(0,0,0)
print(answer if answer<=3 else -1)