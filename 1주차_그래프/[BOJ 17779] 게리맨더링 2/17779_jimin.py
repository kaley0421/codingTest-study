import sys

n = int(input())
_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
total = 0
for row in _map:
    total += sum(row)
answer = int(1e9)

def calc(x,y,d1,d2):
    global total, answer
    cnt = [0] * 5
    # 구역 1
    y1 = y+1
    for r in range(x+d1):
        if r >= x: y1 -= 1
        cnt[0] += sum(_map[r][:y1])

    # 구역 2
    y2 = y+1
    for r in range(x+d2+1):
        if r > x: y2 += 1
        cnt[1] += sum(_map[r][y2:])

    # 구역 3
    y3 = y-d1
    for r in range(x+d1,n):
        cnt[2] += sum(_map[r][:y3])
        if r < x+d1+d2: y3 += 1

    # 구역 4
    y4 = y+d2-n
    for r in range(x+d2+1,n):
        cnt[3] += sum(_map[r][y4:])
        if r <= x+d1+d2: y4 -= 1
    
    # 구역 5
    cnt[4] = total - sum(cnt)
    
    answer = min(answer, max(cnt)-min(cnt))

for x in range(n-2):
    for y in range(1,n-1):
        for d1 in range(1,n-1):
            for d2 in range(1,n-1):
                if 0 <= x+d1-1 < n and 0 <= x+d2-1 < n and 0 <= y-d1+d2-1 < n:
                    if 0 <= y-d1 and y+d2 < n and x+d1+d2 < n:
                        calc(x,y,d1,d2)

print(answer)