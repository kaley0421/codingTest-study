from itertools import combinations

n,m = map(int,input().split())
_map = []
for _ in range(n):
    _map.append(list(map(int,input().split())))

chickens = []
houses = []
for i in range(n):
    for j in range(n):
        if _map[i][j] == 2: chickens.append((i,j))
        if _map[i][j] == 1: houses.append((i,j))

chicken_combis = list(combinations([i for i in range(len(chickens))],m))

answer = 1e9
for chicken_combi in chicken_combis:
    ans_temp = 0
    for h_x,h_y in houses:
        house_min = 1e9
        for i in chicken_combi:
            house_min = min(house_min, abs(h_x-chickens[i][0]) + abs(h_y-chickens[i][1]))
        ans_temp += house_min
    answer = min(answer, ans_temp)

print(answer)