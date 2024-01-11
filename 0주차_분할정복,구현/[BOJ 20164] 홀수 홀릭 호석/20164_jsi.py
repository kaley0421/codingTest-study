from itertools import combinations

L = str(int(input()))
ans_min, ans_max = 1e9, 0

def dfs(_list, answer):
    global ans_min, ans_max

    for i in range(len(_list)):
        answer += int(_list[i]) % 2

    if len(_list) == 1:
        ans_max = max(ans_max, answer)
        ans_min = min(ans_min, answer)
        return

    if len(_list) == 2:
        _sum = int(_list[0]) + int(_list[1])
        
        dfs(list(str(_sum)), answer)
        return
    
    for i, j in combinations(list(range(1, len(_list))), 2):
        _sum = int(''.join(_list[:i])) + int(''.join(_list[i:j])) + int(''.join(_list[j:]))
        
        dfs(str(_sum), answer)

dfs(L, 0)
print(ans_min, ans_max)