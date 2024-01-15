n = int(input())
_dict = dict()
for _ in range(n*n):
    arr = list(map(int,input().split()))
    _dict[arr[0]] = arr[1:]
_map = [[0]*n for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def get_likes(student,cx,cy):
    like_cnt = 0
    for i in range(4):
        if not (0<=cx+dx[i]<n) or not (0<=cy+dy[i]<n): continue
        if _map[cx+dx[i]][cy+dy[i]] in _dict[student]: like_cnt += 1
    return like_cnt

def get_emptys(cx,cy):
    empty_cnt = 0
    for i in range(4):
        if not (0<=cx+dx[i]<n) or not (0<=cy+dy[i]<n): continue
        if _map[cx+dx[i]][cy+dy[i]] == 0: empty_cnt += 1
    return empty_cnt

for student in _dict.keys():
    # 인접한 칸에 좋아하는 학생이 가장 많은 칸으로
    candi1 = []   # (좋아하는 학생 수, i, j)
    for i in range(n):
        for j in range(n):
            if _map[i][j] == 0:
                candi1.append((get_likes(student,i,j), i, j))
    if len(candi1) == 1: 
        _map[candi1[0][1]][candi1[0][2]] = student
        continue
    
    candi1.sort(reverse = True)
    if candi1[0][0] > 0 and candi1[0][0] > candi1[1][0]:
        _map[candi1[0][1]][candi1[0][2]] = student
        continue
    
    # 인접한 칸에 비어있는 칸이 가장 많은 칸으로
    candi2 = []   # (비어있는 칸 수, i, j)
    for s in candi1:
        if s[0] == candi1[0][0]: 
            candi2.append((get_emptys(s[1],s[2]), s[1], s[2]))
    candi2.sort(reverse = True, key = lambda x : (x[0], -x[1], -x[2]))
    
    if candi2[0][0] > candi2[1][0]:
        _map[candi2[0][1]][candi2[0][2]] = student
        continue

    # 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로
    _map[candi2[0][1]][candi2[0][2]] = student

# 학생의 만족도 구하기
answer = 0
for i in range(n):
    for j in range(n):
        student = _map[i][j]
        x = get_likes(student,i,j)
        if x == 1: answer += 1
        elif x == 2: answer += 10
        elif x == 3: answer += 100
        elif x == 4: answer += 1000
print(answer)