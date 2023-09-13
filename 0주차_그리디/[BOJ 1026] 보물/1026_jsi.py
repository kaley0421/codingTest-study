# 큰 수의 가중치를 적게

N = int(input())

L1 = sorted(map(int, int(input().split())))
L2 = sorted(map(int, int(input().split())), reverse=True)

print(sum([i*j for i, j in zip(L1, L2)]))
