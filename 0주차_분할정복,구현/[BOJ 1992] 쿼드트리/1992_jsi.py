N = int(input())
L = [input() for _ in range(N)]
answer = ''

def quad_tree(n, x, y):
    global answer

    if n == 1:
        answer += L[x][y]
        return
    
    is_all_same = True

    for i in range(n):
        if L[x+i][y:y+n].count(L[x][y]) != n:
            is_all_same = False
            break
    
    if is_all_same:
        answer += L[x][y]
        return
    
    answer += '('
    
    for dx in [0, n//2]:
        quad_tree(n//2, x+dx, y)
        quad_tree(n//2, x+dx, y+n//2)

    answer += ')'

quad_tree(N, 0, 0)
print(answer)    
