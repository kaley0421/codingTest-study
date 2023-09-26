N = int(input())
L = []
dragon_curve = [[False] * 101 for _ in range(101)]

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
ndx, ndy = [0, -1, 0, 1], [-1, 0, 1, 0]

for _ in range(N):
    L.append(list(input().split()))

def get_num_of_rectangles():
    cnt = 0
    for j in range(100):
        for i in range(100):
            if dragon_curve[j][i] and dragon_curve[j+1][i] and dragon_curve[j][i+1] and dragon_curve[j+1][i+1]:
                cnt += 1
    return cnt

def get_difference(prev, now):
    # right, up, left, down
    for k in range(4):
        if now[0] - prev[0] == dx[k] and now[1] - prev[1] == dy[k]:
            return [ndx[k], ndy[k]]
    return [0, 0]

def add_to_dragon_curve(point):
    dragon_curve[point[1]][point[0]] = True


for i in range(N):
    prev_x, prev_y, d, g = map(int, L[i])
    prev = [prev_x, prev_y]
    now = [prev_x + dx[d], prev_y + dy[d]]
    point = [prev, now]
    
    add_to_dragon_curve(prev)
    add_to_dragon_curve(now)

    for j in range(1, g+1):
        
        for k in range(2**(j-1)):
            prev, now = point[2**(j-1) - k - 1], point[2**(j-1) - k]
            next = [x+y for x, y in zip(point[-1], get_difference(prev, now))]

            add_to_dragon_curve(next)
            point.append(next)

print(get_num_of_rectangles())