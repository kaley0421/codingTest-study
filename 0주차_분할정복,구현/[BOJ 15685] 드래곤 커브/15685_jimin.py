def get_curve(x,y,d,g):
    if g==0:
        curves.append((x,y))
        curves.append((x+dx[d],y+dy[d]))
        d_stack.append(next_d[d])
        return (x+dx[d], y+dy[d])                   # 한 세대의 끝점 리턴
    else:
        before_gen_end = get_curve(x,y,d,g-1)
        # 이전 세대까지의 curve 를 바탕으로 현 세대 curve 새로 추가
        cursor = before_gen_end
        for i in range(len(d_stack)-1,-1,-1):
            _d = d_stack[i]
            curves.append((cursor[0]+dx[_d], cursor[1]+dy[_d]))
            d_stack.append(next_d[_d])
            cursor = (cursor[0]+dx[_d], cursor[1]+dy[_d])
        return cursor

dx = [1,0,-1,0]
dy = [0,-1,0,1]
next_d = [1,2,3,0]
sx = [0,1,0,1]
sy = [0,0,1,1]

all_curves = set()
curves = []
d_stack = []        # 방향 저장 stack

n = int(input())
for _ in range(n):
    x,y,d,g = map(int,input().split())
    curves.clear()
    d_stack.clear()
    get_curve(x,y,d,g)
    for c in curves: 
        all_curves.add(c)
  
answer = 0
for i in range(100):
    for j in range(100):
        flag = True
        for k in range(4):
            if (i+sx[k], j+sy[k]) not in all_curves:
                flag = False
                break
        if flag == True:
            answer += 1
print(answer)