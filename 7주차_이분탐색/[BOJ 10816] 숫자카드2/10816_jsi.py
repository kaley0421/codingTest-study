N = int(input())
_list_N = list(map(int, input().split()))
M = int(input())
_list_M = list(map(int, input().split()))
D = {}

for i in _list_N:
    D[i] = D.get(i, 0) + 1

for i in _list_M:
    print(D.get(i, 0), end=' ')