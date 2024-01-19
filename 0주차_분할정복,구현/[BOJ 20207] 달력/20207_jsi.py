N = int(input())
L = []
schedule = []

for _ in range(N):
    S, E = map(int, input().split())
    L.append((S, E))

L.sort(key=lambda x:(x[0], x[0]-x[1]))

for i in range(N):
    row = -1

    for j in range(len(schedule)):
        if max(schedule[j]) < L[i][0]:
            row = j
            break
    
    if row == -1:
        schedule.append([])
    
    for j in range(L[i][0], L[i][1] + 1):
        schedule[row].append(j)

answer = 0
seperator = []

for i in range(min(i[0] for i in schedule), max(i[-1] for i in schedule)):
    is_separated = True
    height = -1

    for j in range(len(schedule)):
        if i in schedule[j]:
            is_separated = False
            break
    
    if is_separated:
        seperator.append(i)

seperator.append(max(i[-1] for i in schedule) + 1)

for i in range(len(seperator)):
    start = min(i[0] for i in schedule) + 1
    height = 0
    for j in range(len(schedule)):
        if schedule[j][0] < seperator[i]:
            height += 1
    
    answer += height * (seperator[i] - start + 1)
    
    for j in range(len(schedule)-1, -1, -1):

        while schedule[j]:
            if schedule[j][0] < seperator[i]:
                schedule[j].pop(0)
            else:
                break
        if not schedule[j]:
            schedule.pop(j)

print(answer)