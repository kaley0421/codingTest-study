# 숫자 다 작음 특히 3보다 크면 -1임 -> 완탐
# https://baby-ohgu.tistory.com/3
# 조합으로 풀어보려고 과감하게 지웠는데 사라짐ㅜㅜ

from itertools import combinations

N, M, H = map(int, input().split())
graph = [[False] * (N + 1) for _ in range(H + 1)]
L = []

def move(start):
    x, y = start, 1

    while x <= H:
        if is_ladder_left(x, y):
            x -= 1
        elif is_ladder_right(x, y):
            x += 1
        else:
            y += 1
    return x
        
def is_ladder_right(x, y):
    if x <= N and y <= H and graph[y][x]:
        return x + 1 <= H and graph[y][x+1]
    return False

def is_ladder_left(x, y):
    if x <= N and y <= H and graph[y][x]:
        return 1 <= x - 1 and graph[y][x-1]
    return False

for i in range(M):
    y, x = map(int, input().split())
    graph[y][x] = True
    graph[y][x+1] = True

for j in range(H + 1):
    for i in range(N + 1):
        if graph[j][i] == True:
            i += 1
        else:
            L.append([j, i])
print(L)

for i in range(1, 4):
    cnt = 0
    for b in range(1, H + 1):
        for a in range(1, N + 1):
            if graph[b][a] == True:
                a += 1
                continue


