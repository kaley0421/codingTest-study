'''
[ 주의 ]
idx == len(need_fills) 인 경우, 즉 정답을 찾은 경우 답 출력한 뒤 exit() 안해주면 틀림.
'''
_map = []
for _ in range(9):
    _map.append(list(map(int,input().split())))

def check_promising(x,y,candi):
    # 가로 체크
    for j in range(9):
        if _map[x][j] == candi:
            return False
    # 세로 체크
    for i in range(9):
        if _map[i][y] == candi:
            return False
    # 사각형 체크
    for i in range(3*(x//3),3*(x//3)+3):
        for j in range(3*(y//3),3*(y//3)+3):
            if _map[i][j] == candi:
                return False
    return True

def fill(idx):
    if idx == len(need_fills):
        for i in range(9):
            for j in range(9):
                print(_map[i][j], end = " ")
            print()
        exit()
    else:
        cur_x,cur_y = need_fills[idx][0],need_fills[idx][1]
        
        for num in range(1,10):
            if check_promising(cur_x,cur_y,num):
                _map[cur_x][cur_y] = num
                fill(idx+1)
                _map[cur_x][cur_y] = 0

need_fills = []
for i in range(9):
    for j in range(9):
        if _map[i][j] == 0:
            need_fills.append((i,j))

fill(0)