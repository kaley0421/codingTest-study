n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

def dfs(x, y, n):
    check = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != graph[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end='')
        n = n // 2
        dfs(x, y, n)  # 오른쪽 위
        dfs(x, y + n, n)  # 왼쪽 위
        dfs(x + n, y, n)  # 오른쪽 아래
        dfs(x + n, y + n, n)  # 왼쪽 아래
        print(")", end='')

    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')

dfs(0, 0, n)

"""
from itertools import chain

N = int(input())
L = []

for _ in range(N):
    L.append(list(map(int, input())))

answer = []

def dfs(_list, n):
    global answer
    _sum = sum([sum(i) for i in _list])

    print(_list, n, _sum, answer)

    if _sum == n*n or _sum == 0:
        return [0] if _sum == 0 else [1]
    if n == 2:
        return list(chain(*_list))

    _list_splited = []
    _list_row_column = [[(0, n//2), (0, n//2)], [(0, n//2), (n//2, n)], [(n//2, n), (0, n//2)], [(n//2, n), (n//2, n)]]
    temp = []

    for row, col in _list_row_column:
        _list_splited.clear()

        for i in range(row[0], row[1]):
            _list_splited.append(_list[i][col[0]:col[1]])
        
        _sum = sum([sum(i) for i in _list_splited])

        # if _sum == 0 or _sum == (n//2)**2:
        #     temp.append(0 if _sum == 0 else 1)
        #     continue
        a = dfs(_list_splited, n//2)
        temp.append(a)
    answer.append(temp)
    

dfs(L, N)
print(answer)
"""