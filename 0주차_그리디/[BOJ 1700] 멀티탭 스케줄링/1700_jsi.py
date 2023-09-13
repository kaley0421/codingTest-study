N, K = map(int, input().split())
L = list(map(int, input().split()))
A = [0 for _ in range(N)]
answer = 0

def solution(i):
    # 1. 콘센트가 이미 꽂혀있다면
    if L[i] in A:
        return 0
    # 2. 콘센트가 비어있다면
    elif 0 in A:
        A[A.index(0)] = L[i]
        return 0
    # 3. 교체해야 함
    else:
        for j in range(N):
            if A[j] not in L[i+1:]:   # 3-1. 더 이상 사용 안 하는 게 있다면 바꿈 -> 바꿈
                A[j] = L[i]
                return 1
    
    # 3-2. 나중에 재사용할 것들만 있음 -> 순서 판별해야 함(가장 나중에 쓸 것을 뽑음)
    orders = []
    for j in range(N):
        orders.append((i + L[i:].index(A[j]), j))
    
    orders = sorted(orders, reverse=True)
    A[orders[0][1]] = L[i]
    return 1
          
for i in range(K):
    answer += solution(i)

print(answer)