r,c,k = map(int,input().split())
a = []
for _ in range(3):
    a.append(list(map(int,input().split())))

def sort_line(line):
    sort_dict = dict()
    for l in line:
        if l not in sort_dict: sort_dict[l] = 1
        else: sort_dict[l] += 1
    
    sort_tuples = []
    for key in sort_dict.keys():
        sort_tuples.append((key,sort_dict[key]))
    sort_tuples.sort(key = lambda x: (x[1],x[0]))

    result = []
    for t in sort_tuples:
        if t[0] != 0:
            result.append(t[0])
            result.append(t[1])
    
    return result

def _r():
    global a,n,m
    appending = []
    new_m = 0

    for i in range(n):
        arr = sort_line(a[i])
        appending.append(arr)
        new_m = max(new_m, len(arr))
    
    # 원 배열 갱신
    a = [[0]*new_m for _ in range(n)]
    for i in range(n):
        for j in range(len(appending[i])):
            a[i][j] = appending[i][j]

    # n,m 값 갱신
    m = new_m

def _c():
    global a,n,m
    appending = []
    new_n = 0

    for j in range(m):
        ori = []
        for i in range(n):
            ori.append(a[i][j])
        arr = sort_line(ori)
        appending.append(arr)
        new_n = max(new_n,len(arr))

    # 원 배열 갱신
    a = [[0]*m for _ in range(new_n)]
    for j in range(m):
        for i in range(len(appending[j])):
            a[i][j] = appending[j][i]

    # n,m 값 갱신
    n = new_n

def validate():
    global a,n,m

    if n>100 and m>100:
        new_a = [[0]*100 for _ in range(100)]
        for i in range(100):
            for j in range(100):
                new_a[i][j] = a[i][j]
        a = new_a
    elif n>100:
        new_a = [[0]*m for _ in range(100)]
        for i in range(100):
            for j in range(m):
                new_a[i][j] = a[i][j]
        a = new_a
    elif m>100:
        new_a = [[0]*100 for _ in range(n)]
        for i in range(n):
            for j in range(100):
                new_a[i][j] = a[i][j]
        a = new_a

time = 0
n,m = 3,3
while time <= 100:
    if 0<=r-1<n and 0<=c-1<m and a[r-1][c-1] == k:
        break

    if n>=m: _r()
    else: _c()

    validate()
    time += 1

if time > 100:
    print(-1)
else:
    print(time)