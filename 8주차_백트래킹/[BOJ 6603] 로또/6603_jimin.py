''' 1. combinations 사용
'''
# from itertools import combinations

# while True:
#     _list = list(map(int,input().split()))
#     k = _list[0]
#     if k == 0: break
#     s = _list[1:]

#     combi_s = list(combinations(s,6))
#     combi_s.sort()

#     for i in range(len(combi_s)):
#         print(' '.join(map(str,combi_s[i])))
#     print()


''' 2. 백트래킹 사용
'''
def dfs(idx):
    if len(lotto) == 6:
        print(' '.join(map(str,lotto)))
        return

    for i in range(idx,k):
        if s[i] not in lotto:
            if len(lotto)==0 or (len(lotto)>0 and s[i] > lotto[-1]):
                lotto.append(s[i])
                dfs(idx+1)
                lotto.pop()

while True:
    _list = list(map(int,input().split()))
    k = _list[0]
    if k == 0: break
    s = _list[1:]

    s.sort()
    lotto = []

    dfs(0)

    print()