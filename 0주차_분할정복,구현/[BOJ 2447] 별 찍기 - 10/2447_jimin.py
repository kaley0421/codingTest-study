n = int(input())

answer = [['*'] * n for _ in range(n)]

def process(n,s_x,s_y):
    if n < 3: return

    # 가장자리 채우기
    base = n // 3
    for x in range(0,n,base):
        for y in range(0,n,base):
            process(base, s_x+x, s_y+y)

     # 가운데 구멍
    for i in range(0,n//3):
        for j in range(0,n//3):
            answer[s_x+base+i][s_y+base+j] = " "

process(n, 0, 0)

for line in answer: 
    print(''.join(line))