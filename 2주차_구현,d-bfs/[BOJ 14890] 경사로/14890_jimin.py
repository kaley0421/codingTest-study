n,l = map(int,input().split())
_map = []
for _ in range(n):
    _map.append(list(map(int,input().split())))

answer = 0

bingo_row = set()
bingo_col = set()

visited = [[False] * n for _ in range(n)]
# 한 행씩 체크
for i in range(n):
    # 해당 행이 모두 같은지 체크
    flag = True
    for j in range(n):
        if _map[i][j] != _map[i][0]:
            flag = False
            break
    if flag == True: 
        answer += 1
        bingo_row.add(i)
    
    # 경사로 놓을 수 있는지 체크
    flag = True
    j = 0
    while j < n-1:
        if _map[i][j] != _map[i][j+1]:
            if abs(_map[i][j] - _map[i][j+1]) != 1:
                flag = False
                break
            else:
                # j < j+1 인 경우
                if _map[i][j] < _map[i][j+1]:
                    for k in range(j,j-l,-1):
                        # 경사로가 맵을 벗어나는 경우
                        if not 0<=k<n:
                            flag = False
                            break
                        # 경사로 놓는 바닥면 높이가 일정하지 않은 경우
                        if _map[i][k] != _map[i][j]:
                            flag = False
                            break
                    if flag == False: break

                    # 경사로 놓음 체크
                    for k in range(j,j-l,-1):
                        if visited[i][k] == True:
                            flag = False
                            break
                        visited[i][k] = True
                    if flag == False: break

                    j += 1
                # j > j+1 인 경우
                else:
                    for k in range(j+1,j+l+1):
                        # 경사로가 맵을 벗어나는 경우
                        if not 0<=k<n:
                            flag = False
                            break
                        # 경사로 놓는 바닥면 높이가 일정하지 않은 경우
                        if _map[i][k] != _map[i][j+1]:
                            flag = False
                            break
                    if flag == False: break

                    # 경사로 놓음 체크
                    for k in range(j+1,j+l+1):
                        if visited[i][k] == True:
                            flag = False
                            break
                        visited[i][k] = True
                    if flag == False: break

                    j = j + l
        else:
            j += 1
    
    if flag == True: 
        if i not in bingo_row:
            answer += 1


visited = [[False] * n for _ in range(n)]
# 한 열씩 체크
for j in range(n):
    # 해당 열이 모두 같은지 체크
    flag = True
    for i in range(n):
        if _map[i][j] != _map[0][j]:
            flag = False
            break
    if flag == True:
        answer += 1
        bingo_col.add(j)
    
    # 경사로 놓을 수 있는지 체크
    flag = True
    i = 0
    while i < n-1:
        if _map[i][j] != _map[i+1][j]:
            if abs(_map[i][j] - _map[i+1][j]) != 1:
                flag = False
                break
            else:
                # i < i+1 인 경우
                if _map[i][j] < _map[i+1][j]:
                    for k in range(i,i-l,-1):
                        # 경사로가 맵을 벗어나는 경우
                        if not 0<=k<n:
                            flag = False
                            break
                        # 경사로 놓는 바닥면 높이가 일정하지 않은 경우
                        if _map[k][j] != _map[i][j]:
                            flag = False
                            break
                    if flag == False: break

                    # 경사로 놓음 체크
                    for k in range(i,i-l,-1):
                        if visited[k][j] == True:
                            flag = False
                            break
                        visited[k][j] = True
                    if flag == False: break

                    i += 1
                # i > i+1 인 경우
                else:
                    for k in range(i+1,i+l+1):
                        # 경사로가 맵을 벗어나는 경우
                        if not 0<=k<n:
                            flag = False
                            break
                        # 경사로 놓는 바닥면 높이가 일정하지 않은 경우
                        if _map[k][j] != _map[i+1][j]:
                            flag = False
                            break
                    if flag == False: break

                    # 경사로 놓음 체크
                    for k in range(i+1,i+l+1):
                        if visited[k][j] == True:
                            flag = False
                            break
                        visited[k][j] = True
                    if flag == False: break

                    i = i + l
        else:
            i += 1

    if flag == True:
        if j not in bingo_col:
            answer += 1

print(answer)