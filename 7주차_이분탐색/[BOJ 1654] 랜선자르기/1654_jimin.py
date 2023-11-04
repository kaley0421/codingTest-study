k,n = map(int,input().split())
lans = []
for _ in range(k):
    lans.append(int(input()))

lans.sort()

def make_cnt(length):
    cnt = 0
    for l in lans: cnt += l // length
    return cnt

start,end = 1,lans[-1]
answer = 0
while start <= end:
    mid = (start+end) // 2
    cnt = make_cnt(mid)
    if cnt >= n:
       start = mid+1
       answer = max(answer,mid)
    else:
        end = mid-1

print(answer)