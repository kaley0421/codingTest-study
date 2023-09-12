# ---------------------------------------------------- 1트 => 틀림
# 1. '앞으로 해당 전자기기가 몇번 더 사용되는지' 빈도수를 기준으로 풀이
# 2. 반례: 1 2 3 4 3 4 2 2 인 경우
# ----------------------------------------------------
# from collections import deque

# n,k = map(int,input().split())
# uses = list(map(int,input().split()))

# use_q = deque(uses)
# plugs = [0] * n

# use_left = dict()
# for u in uses:
#     if u in use_left: use_left[u] += 1
#     else: use_left[u] = 1

# for i in range(n):
#     _cur = use_q.popleft()
#     plugs[i] = _cur
#     use_left[_cur] -= 1

# print("plugs: ", plugs)
# print("use_left: ",use_left)

# answer = 0

# while use_q:
#     _next = use_q.popleft()

#     print("=== next: ", _next)

#     # 플러그 유지
#     if _next in plugs: 
#         use_left[_next] -= 1
#         continue

#     # 기존 플러그 뽑고 교체
#     flag = False
#     for i in range(n):
#         # 앞으로 더이상 사용되지 않는 플러그 뽑기
#         if use_left[plugs[i]] == 0:
#             plugs[i] = _next
#             use_left[_next] -= 1
#             flag = True
#     if flag == False:
#         plugs[0] = _next
#         use_left[_next] -= 1
    
#     answer += 1

#     print("--- plugs: ", plugs)
#     print("--- answer: ", answer)

# print(answer)
            
        
# ---------------------------------------------------- 2트
# 1. '현재 플러그에 꽂혀있는 기기들 중 가장 나중에 재사용될 기기' 를 우선적으로 플러그에서 뽑는다.
# ----------------------------------------------------
from collections import deque

def plug_to_pop():
    global n
    farest = 0
    poping_idx = 0

    for i in range(n):
        # 이렇게 해도 가능 (index 함수 이용)
        # target = plugs[i]

        # if target not in use_q:
        #     poping_idx = i
        #     return poping_idx
        
        # if use_q.index(target) > farest:
        #     farest = use_q.index(target)
        #     poping_idx = i

        temp = 0
        for j in range(len(use_q)):
            if plugs[i] == use_q[j]: break
            temp += 1
        
        if temp > farest:
            farest = temp
            poping_idx = i

    return poping_idx

n,k = map(int,input().split())
uses = list(map(int,input().split()))

use_q = deque(uses)
plugs = [0] * n

if n >= k:
    print(0)
    exit()

for i in range(n):
    _cur = use_q.popleft()
    if _cur in plugs: continue
    plugs[i] = _cur
   
answer = 0
while use_q:
    _next = use_q.popleft()

    # 플러그 유지
    if _next in plugs: continue

    if 0 in plugs:
        # 비어있는 플러그가 있는 경우
        plugs[plugs.index(0)] = _next
    else:
        # 기존 플러그 뽑고 교체
        poping_idx = plug_to_pop()
        plugs[poping_idx] = _next
        answer += 1

print(answer)