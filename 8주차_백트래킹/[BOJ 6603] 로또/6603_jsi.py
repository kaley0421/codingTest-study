from itertools import combinations

S = list(map(int, input().split()))

while len(S) != 1:
    K = S[0]
    S.pop(0)
    
    for comb in combinations(S, 6):
        print(' '.join(map(str, comb)))
    print()
    
    S = list(map(int, input().split()))
