''' 1트 => 안되는데 왜 안되는지 모르겠다! 대충 답이랑 구현법은 똑같은거 같은데 ㅜㅜ

_map = []
for _ in range(9):
    _map.append(list(map(int,input())))

nodes = []
for i in range(9):
    for j in range(9):
        if _map[i][j] == 0:
            nodes.append((i,j))

print("!!!! nodes length: ", len(nodes))

def get_candi(x,y):
    row_need = set([1,2,3,4,5,6,7,8,9])
    col_need = set([1,2,3,4,5,6,7,8,9])
    square_need = set([1,2,3,4,5,6,7,8,9])

    for i in range(9):
        if _map[x][i] in row_need:
            row_need.remove(_map[x][i])
    
    for i in range(9):
        if _map[i][y] in col_need:
            col_need.remove(_map[i][y])

    for i in range(3):
        for j in range(3):
            if _map[3*(x//3) + i][3*(y//3) + j] in square_need:
                square_need.remove(_map[3*(x//3) + i][3*(y//3) + j])

    print("--- row_need: ", row_need)
    print("--- col need: ", col_need)
    print("--- square_need: ", square_need)

    candi_fill = []
    for i in range(9):
        if i in row_need and i in col_need and i in square_need:
            candi_fill.append(i)
    
    print("--- candi: ", candi_fill)
    return candi_fill


def check_row(x):
    check = [0] * (10)
    for i in range(9):
        if check[_map[x][i]] == 0:
            check[_map[x][i]] = 1
        elif _map[x][i] == 0:
            continue
        else:
            return False
    return True

def check_col(y):
    check = [0] * (10)
    for i in range(9):
        if check[_map[i][y]] == 0:
            check[_map[i][y]] = 1
        elif _map[i][y] == 0:
            continue
        else:
            return False
    return True

def check_square(x,y):
    check = [0] * (10)
    for i in range(3):
        for j in range(3):
            if check[_map[3*(x//3) + i][3*(y//3) + j]] == 0:
                check[_map[3*(x//3) + i][3*(y//3) + j]] = 1
            elif _map[3*(x//3) + i][3*(y//3) + j] == 0:
                continue
            else:
                return False
    return True

def write(node_idx):
    x, y = nodes[node_idx][0], nodes[node_idx][1]

    print("==== node_idx: ", node_idx)
    print("=== x,y: ", x,y)

    # promising check
    flag = True
    flag = check_row(x)
    print("=== promise flag 1: ", flag)
    flag = check_col(y)
    print("=== promise flag 2: ", flag)
    flag = check_square(x,y)

    print("=== promise flag 3: ", flag)

    # 마지막 노드에 도달했고, 정답인 경우
    if flag == True and node_idx == len(nodes):
        print("############## reach answer !!!")
        for i in range(9):
            for j in range(9):
                print(_map[i][j], end = " ")
            print()
        exit()

    if flag == True:            # 다음 노드 탐색
        print("############## map before going next node")
        for i in range(9):
            for j in range(9):
                print(_map[i][j], end = " ")
            print()

        candis = get_candi(x,y)
        for candi in candis:
            _map[x][y] = candi
            write(node_idx+1)
            _map[x][y] = 0
    else:                       # flag == false -> backtrack
        return

write(0)
'''


''' 2트 => 구글링 후 코드 수정
[ 답과의 차이점 ]
1. 답에서는 get_candi 함수를 굳이 쓰지 않고 1~9 까지를 그냥 다 넣어보며 dfs 돌린다.
    - 1트에서 get_candi 함수 결과 빈칸에 채워넣을 숫자를 구하는데, 해당 배열이 빈 배열인 경우 더이상 탐색을 진행하지 않는 문제 있었음
2. check_row, check_col, check_square 함수 로직 차이
    - 단순히 해당 num 이 해당 행/열/사각형 내에 존재하는지 아닌지 체킹만 해주면 됨
3. promising 체킹 시점
    - 왜 문제가 되지 ??
'''
_map = []
for _ in range(9):
    _map.append(list(map(int,input())))

nodes = []
for i in range(9):
    for j in range(9):
        if _map[i][j] == 0:
            nodes.append((i,j))

def check_row(r, num):
    for x in range(9):
        if num == _map[r][x]:
            return False
    return True

def check_col(c, num):
    for x in range(9):
        if num == _map[x][c]:
            return False
    return True

def check_square(r, c, num):
    nc = (c // 3) * 3
    nr = (r // 3) * 3
    for x in range(3):
        for y in range(3):
            if _map[nr + x][nc + y] == num:
                return False
    return True

def write(node_idx):
    if node_idx >= len(nodes):
        for k in range(9):
            print(''.join(map(str, _map[k])))
        exit()

    x, y = nodes[node_idx][0], nodes[node_idx][1]

    for candi in range(1,10):
        if check_row(x,candi) and check_col(y,candi) and check_square(x,y,candi):
            _map[x][y] = candi
            write(node_idx+1)
            _map[x][y] = 0    


write(0)