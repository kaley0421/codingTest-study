import sys
sys.setrecursionlimit(10**6)

n = int(input())
_map = []
for _ in range(n):
    _map.append(list(map(int,input().split())))

ans_blue, ans_white = 0, 0

def check_same(x_s,x_e,y_s,y_e):
    global ans_blue, ans_white
    for i in range(x_s, x_e):
        for j in range(y_s, y_e):
            if _map[x_s][y_s] != _map[i][j]:
                return False
    if _map[x_s][y_s] == 1: ans_blue += 1
    else: ans_white += 1
    return True

def process(x_s,x_e,y_s,y_e):
    if check_same(x_s,x_e,y_s,y_e) == False:
        process(x_s, x_s+(x_e-x_s)//2, y_s, y_s+(y_e-y_s)//2)
        process(x_s+(x_e-x_s)//2, x_e, y_s, y_s+(y_e-y_s)//2)
        process(x_s, x_s+(x_e-x_s)//2, y_s+(y_e-y_s)//2, y_e)
        process(x_s+(x_e-x_s)//2, x_e, y_s+(y_e-y_s)//2, y_e)

process(0,n,0,n)

print(ans_white)
print(ans_blue)