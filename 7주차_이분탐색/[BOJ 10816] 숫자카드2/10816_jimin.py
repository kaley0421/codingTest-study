''' 1트 => 이분탐색 사용. 시간초과
'''
# import sys
# sys.setrecursionlimit(10**6)

# n = int(input())
# cards = list(map(int,input().split()))
# m = int(input())
# target = list(map(int,input().split()))

# def binary_search(start,end,target):
#     global cnt

#     mid = (start+end) // 2

#     if not 0<=start<=mid<=end<=n-1: return

#     if cards[mid] == target:
#         if flag[mid] == False:
#             flag[mid] = True
#             cnt += 1
#             binary_search(start,mid-1,target)
#             binary_search(mid+1,end,target)
    
#     if cards[mid] > target:
#         binary_search(start,mid-1,target)
#     else:
#         binary_search(mid+1,end,target)

# cards.sort()

# cnt = 0
# flag = [False] * n

# for t in target:
#     cnt = 0
#     flag = [False] * n
#     binary_search(0,n-1,t)
#     print(cnt, end=" ")


''' 2트
'''
# from collections import defaultdict

# n = int(input())
# cards = list(map(int,input().split()))
# m = int(input())
# target = list(map(int,input().split()))

# card_dict = defaultdict(int)
# for card in cards:
#     card_dict[card] += 1

# for t in target:
#     print(card_dict[t], end = " ")


''' 3트 => 이분탐색 사용.
1. 이분탐색은 정렬된 배열에 대해 진행하므로, target 값을 찾은 경우 & 같은 target 값이 여러 개 있을 경우에,
    해당 target 값들은 start 와 end 사이에 있을 것.
2. 찾은 target 값들은 dict 에 저장해 놔서, dict 에 값이 존재하는 경우 가져온다 <- 시간 효율 향상
'''
from collections import defaultdict

n = int(input())
cards = list(map(int,input().split()))
m = int(input())
target = list(map(int,input().split()))

def binary_search(target):
    global cnt
    start, end = 0, n-1

    while start<=end:
        mid = (start+end) // 2

        if cards[mid] == target:
            cnt = cards[start:end+1].count(target)
            return
    
        if cards[mid] > target:
            end = mid-1
        else:
            start = mid+1

cards.sort()

card_cnt = defaultdict(int)
cnt = 0
for t in target:
    if t not in card_cnt:
        cnt = 0
        binary_search(t)
        card_cnt[t] = cnt
    print(card_cnt[t], end=" ")