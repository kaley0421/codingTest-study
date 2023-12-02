from itertools import combinations

N = int(input())
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cnt = 0

for i in range(1, 11):
    L = list(combinations(number, i))
    total = len(L) + cnt
    
    if N < total:
        L_sorted = sorted([''.join(map(str, i))[::-1] for i in L])
        print(L_sorted[N-cnt])
        exit()
    else:
        cnt = total
print(-1)