n,b = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))

def multi(x,y):        # 두 행렬을 곱한 결과 반환
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += x[i][k] * y[k][j] % 1000
    return res

def process(x,cnt):
    if cnt == 1: return x
    res = process(x,cnt//2)
    if cnt % 2 == 0: return multi(res,res)
    else: return multi(multi(res,res),x)

ans = process(a,b)

for i in range(n):
    for j in range(n):
        print(ans[i][j] % 1000, end = " ")
    print()