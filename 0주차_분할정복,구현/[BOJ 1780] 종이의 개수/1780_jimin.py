n = int(input())
_map = []
for _ in range(n):
    _map.append(list(map(int,input().split())))

answer = [0,0,0]

def check(n,x_s,y_s):
    for i in range(n):
        for j in range(n):
            if _map[x_s][y_s] != _map[x_s+i][y_s+j]:
                return False
    return True

def cut(n,x_s,y_s):
    if check(n,x_s,y_s):
        answer[_map[x_s][y_s]+1] += 1
        return

    # 9개로 쪼개기
    for i in range(0,n,n//3):
        for j in range(0,n,n//3):
            cut(n//3,x_s+i,y_s+j)

cut(n,0,0)

for ans in answer: print(ans)