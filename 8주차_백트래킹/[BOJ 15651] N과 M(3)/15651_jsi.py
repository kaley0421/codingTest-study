from itertools import product

N, M = map(int, input().split())
L = list(range(1, N + 1))

for i in product(L, repeat=M):
    print(' '.join(map(str, i)))