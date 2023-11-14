L = []
_list_to_fill = []

for i in range(9):
    L.append(list(map(int, input().split())))
    
    for j in range(9):
        if L[i][j] == 0:
            _list_to_fill.append((i, j))

def is_promising(x, y, num):

    for i in range(9):
        if L[i][y] == num:
            return False
    
    for j in range(9):
        if L[x][j] == num:
            return False
    
    for i in range((x//3)*3, (x//3)*3 + 3):
        for j in range((y//3)*3, (y//3)*3 + 3):
            if L[i][j] == num:
                return False
    return True

def solve(idx):
    if idx == len(_list_to_fill):
        for i in range(9):
            print(*L[i])
        exit()

    for num in range(1, 10):
        x, y = _list_to_fill[idx]

        if is_promising(x, y, num):
            L[x][y] = num
            solve(idx + 1)
            L[x][y] = 0

solve(0)