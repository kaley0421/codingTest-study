''' product 활용
'''
from itertools import product

n,m = map(int,input().split())
_list = [i for i in range(1,n+1)]

result = list(product(_list, repeat=m))
result.sort()

for r in result:
    for i in range(len(r)):
        print(r[i], end = " ")
    print()


''' 백트래킹 활용
'''
n,m = map(int,input().split())

_list = []

def dfs():
    if len(_list) == m:
        print(' '.join(map(str,_list)))
        return

    for i in range(1,n+1):
        _list.append(i)
        dfs()
        _list.pop()

dfs()