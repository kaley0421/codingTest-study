# 리스트 길이가 1개일 경우 생각하기
# max 사용 불가

from copy import deepcopy

N = int(input())
_list = []
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

for _ in range(N):
    _list.append(list(map(int, input().split())))

def move_right(graph):
    for i in range(N):
        new_list = []

        for j in range(N):
            if graph[i][j] != 0:
                new_list.append(graph[i][j])
        graph[i] = [0] * (N - len(new_list)) + new_list

        idx = N - 1

        while 0 < idx:
            if graph[i][idx] == graph[i][idx-1]:
                graph[i][idx] *= 2
                graph[i][idx-1] = 0
                idx -= 1
            idx -= 1

        new_list = []

        for j in range(N):
            if graph[i][j] != 0:
                new_list.append(graph[i][j])
        
        graph[i] = [0] * (N - len(new_list)) + new_list

def move_left(graph):
    for i in range(N):
        new_list = []
        idx = 0

        for j in range(N):
            if graph[i][j] != 0:
                new_list.append(graph[i][j])
        
        graph[i] = new_list + [0] * (N - len(new_list))

        while idx < N - 1:
            if graph[i][idx] == graph[i][idx+1]:
                graph[i][idx] *= 2
                graph[i][idx+1] = 0
                idx += 1
            idx += 1
        
        new_list = []
        
        for j in range(N):
            if graph[i][j] != 0:
                new_list.append(graph[i][j])
        
        graph[i] = new_list + [0] * (N - len(new_list))
            
def move_up(graph):
    for i in range(N):
        idx = 0
        new_list = []

        for j in range(N):
            if graph[j][i] != 0:
                new_list.append(graph[j][i])
        
        for j in range(len(new_list)):
            graph[j][i] = new_list[j]
        for j in range(len(new_list), N):
            graph[j][i] = 0

        while idx < N-1:
            if graph[idx][i] == graph[idx+1][i]:
                graph[idx][i] *= 2
                graph[idx+1][i] = 0
                idx += 1
            idx += 1

        new_list = []

        for j in range(N):
            if graph[j][i] != 0:
                new_list.append(graph[j][i])
        
        for j in range(len(new_list)):
            graph[j][i] = new_list[j]
        for j in range(len(new_list), N):
            graph[j][i] = 0

def move_down(graph):
    for i in range(N):
        idx = N-1
        new_list = []

        for j in range(N):
            if graph[j][i] != 0:
                new_list.append(graph[j][i])
        
        for j in range(N-1 , N-len(new_list)-1, -1):
            graph[j][i] = new_list[j - (N-len(new_list))]
        for j in range(N-len(new_list)-1, -1, -1):
            graph[j][i] = 0
        
        while 0 < idx:
            if graph[idx][i] == graph[idx-1][i]:
                graph[idx][i] *= 2
                graph[idx-1][i] = 0
                idx -= 1
            idx -= 1

        new_list = []

        for j in range(N):
            if graph[j][i] != 0:
                new_list.append(graph[j][i])
        
        for j in range(N-1 , N-len(new_list)-1, -1):
            graph[j][i] = new_list[j - (N-len(new_list))]
        for j in range(N-len(new_list)-1, -1, -1):
            graph[j][i] = 0

def is_equal(graph1, graph2):
    for i in range(N):
        for j in range(N):
            if graph1[i][j] != graph2[i][j]:
                return False
    return True

def merge(graph, dir):
    if dir == UP:
        move_up(graph)
    elif dir == DOWN:
        move_down(graph)
    elif dir == LEFT:
        move_left(graph)
    elif dir == RIGHT:
        move_right(graph)

answer = _list[0][0]

def dfs(depth, graph):
    global answer
    
    if depth == 4:
        for i in range(N):
            answer = max(max(graph[i]), answer)
        return

    for dir in [UP, DOWN, LEFT, RIGHT]:
        graph_copy = deepcopy(graph)

        merge(graph_copy, dir)
        print(depth, dir, answer)
        print(graph_copy)
        if is_equal(graph_copy, graph):
            for i in range(N):
                answer = max(max(graph[i]), answer)
        else:
            dfs(depth+1, graph_copy)
dfs(0, _list)
print(answer)
