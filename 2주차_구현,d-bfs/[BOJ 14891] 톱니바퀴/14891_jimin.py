from collections import deque

def wheel_turn(tar,direct):
    if direct == 1:
        wheel[tar].appendleft(wheel[tar].pop())
    else:
        wheel[tar].append(wheel[tar].popleft())

def is_turn(left,right):
    if left == 0 or right == 5: return False
    if wheel[left][2] != wheel[right][6]: return True
    return False

def process(target,direction):
    visited = [False] * (5)
    visited[target] = True

    q = deque([(target+1,direction,is_turn(target,target+1)), (target-1,direction,is_turn(target-1, target))])
    
    wheel_turn(target,direction)

    while q:
        cur, before_direct, turn_flag = q.popleft()
        cur_direct = -1 * before_direct

        if 1 <= cur <= 4 and visited[cur] == False:
            visited[cur] = True
            # 맞닿은 톱니의 극이 다르면, 이전 톱니의 반대방향으로 회전 -> 회전 큐에 넣기
            if turn_flag == True:
                q.append((cur+1,cur_direct,is_turn(cur,cur+1)))
                q.append((cur-1,cur_direct,is_turn(cur-1,cur)))
                wheel_turn(cur,cur_direct)

wheel = [[]]
for i in range(1,5):
    wheel.append(deque(list(input())))

k = int(input())
for _ in range(k):
    target, direction = map(int,input().split())
    process(target,direction)

answer = 0
if wheel[1][0] == '1': answer += 1
if wheel[2][0] == '1': answer += 2
if wheel[3][0] == '1': answer += 4
if wheel[4][0] == '1': answer += 8
print(answer)