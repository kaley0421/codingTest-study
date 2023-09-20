from collections import deque

def score():
    answer = 0
    for i in range(4):
        if L[i][0] == 1:
            answer += 2**i
    return answer

def rotate(n, clockwise):
    print(n, clockwise)
    print(L[n])
    if clockwise == 1:
        L[n].appendleft(L[n].pop())
    else:
        L[n].append(L[n].popleft())
    print(L[n])
    
    

def is_available(n, right):
    if right == 1:
        return L[n][2] == L[n+1][-2]
    else:
        return L[n][-2] == L[n-1][2]


L = [deque(list(map(int, input()))) for _ in range(4)]
K = int(input())
RIGHT, LEFT = 1, 0

for i in range(K):
    num, dir = map(int, input().split())
    num -= 1

    rotate(num, dir)

    if num == 0:
        for j in [1, 2, 3]:
            if not is_available(j-1, RIGHT):
                break
            rotate(j, dir)
    elif num == 3:
        for j in [2, 1, 0]:
            if not is_available(j+1, LEFT):
                break
            rotate(j, dir)
    elif num == 2:
        if is_available(2, RIGHT):
            rotate(3, dir)
        if is_available(2, LEFT):
            rotate(1, dir)
        else:
            continue
        if is_available(1, LEFT):
            rotate(0, dir)
    elif num == 1:
        if is_available(1, LEFT):
            rotate(0, dir)
        if is_available(1, RIGHT):
            rotate(2, dir)
        else:
            continue
        if is_available(2, RIGHT):
            rotate(3, dir)
    print(L)
print(score())