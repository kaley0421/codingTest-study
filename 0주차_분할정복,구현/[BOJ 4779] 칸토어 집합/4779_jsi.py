def dfs(n, _list):
    if n == 0:
        return ['-']
    
    return dfs(n-1, _list[:3**(n-1)]) + [' ' * (3**(n-1))] + dfs(n-1, _list[2*3**(n-1):])

while True:
    try:
        N = int(input())
        L = ['-' * (3**N)]
        answer = dfs(N, L)
        print(''.join(answer))
    
    except:
        break