n = int(input())
_map = []
for _ in range(n):
    _map.append(list(map(int,input())))

answer = ""

def check(start_x, start_y, n):
    for i in range(n):
        for j in range(n):
            if _map[start_x][start_y] != _map[start_x+i][start_y+j]:
                return False
    return True

def process(start_x, start_y, n):
    global answer

    if check(start_x, start_y, n):
        answer += str(_map[start_x][start_y])
        return

    answer += "("
    process(start_x, start_y, n//2)
    process(start_x, start_y+n//2, n//2)
    process(start_x+n//2, start_y, n//2)
    process(start_x+n//2, start_y+n//2, n//2)
    answer += ")"

process(0,0,n)

print(answer)