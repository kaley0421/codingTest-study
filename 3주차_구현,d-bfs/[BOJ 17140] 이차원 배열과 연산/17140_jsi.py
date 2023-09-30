r, c, k = map(int, input().split())
A = []

for i in range(3):
    A.append(list(map(int, input().split())))

def fill(A):
    len_row = len(A)
    len_col = max([len(A[i]) for i in range(len(A))])

    for i in range(len_row):
        if len(A[i]) != len_col:
            A[i].extend([0 for _ in range(len_col - len(A[i]))])
        if len(A[i]) > 100:
            A[i] = A[i][:100]
    
    return A[:min(len_row, 100)]

def sort_list(L):
    D = dict()
  
    for i in L:
        if i == 0:
            continue
        D[i] = D.get(i, 0) + 1

    _list = sorted(D.items(), key=lambda x:(x[1], x[0]))
    return [i for item in _list for i in item]

def start_r(A):
    for i in range(len(A)):
        A[i] = sort_list(A[i])
    
    return fill(A)

def start_c(A):
    arr, sorted_arr = [], []

    for i in range(len(A[0])):
        temp = []
        for j in range(len(A)):
            if A[j][i] == 0:
                continue
            temp.append(A[j][i])
        arr.append(temp)
    
    sorted_arr = start_r(arr)

    arr = [[] for _ in range(len(sorted_arr[0]))]

    for i in range(len(sorted_arr[0])):
        for j in range(len(sorted_arr)):
            arr[i].append(sorted_arr[j][i])
    return arr

def dfs(A, depth):
    if len(A) >= r and len(A[0]) >= c and A[r-1][c-1] == k:
        print(depth)
        return
    
    if depth >= 100:
        print(-1)
        return

    depth += 1    
    if len(A) >= len(A[0]):
        dfs(start_r(A), depth)
    else:
        dfs(start_c(A), depth)

dfs(A, 0)

