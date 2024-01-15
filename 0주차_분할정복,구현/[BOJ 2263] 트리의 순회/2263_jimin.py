''' 1트 => 왜 틀렸는지 모르겠
'''
# n = int(input())

# _in = list(map(int,input().split()))
# _post = list(map(int,input().split()))

# root_in = [False]*len(_in)
# root_post = [False]*len(_post)

# answer = []
# answer.append(_post[-1])

# def process(root, _in, _post):
#     global answer

#     if len(answer) == len(_in): return

#     # if (root 가 리프노드인 경우) answer 에 더한다.
#     # : InOrder 배열에서 앞뒤 원소가 모두 root 인 경우
#     if len(_in)==1 and len(_post)==1 and _in[0]==_post[0]:
#         #answer.append(root)
#         return

#     # _in 에서 root 를 기준으로 left_in, right_in 나누기
#     left_in, right_in = _in[:_in.index(root)], _in[_in.index(root)+1:]

#     # post 에서 left_in, right_in 각각의 루트노드 찾기
#     bound_idx, left_root, right_root = 0, 0, 0
#     if len(_post) == 2:
#         if _in.index(_post[0]) < _in.index(_post[1]):
#             left_root = _post[0]
#         else:
#             right_root = _post[0]
#     else:
#         for i in range(len(_post)-2,-1,-1):
#             if _post[i] not in right_in: break
#             else: bound_idx = i
#         left_root = _post[bound_idx-1]
#         right_root = _post[-2]

#     # left_in 루트 찾고, answer 에 더하고, 하위 탐색
#     if len(left_in)>0:
#         answer.append(left_root)
#         if len(_post) == 2:
#             process(left_root, left_in, [_post[0]])
#         else:
#             process(left_root, left_in, _post[:bound_idx])

#     # right_in 루트 찾고, answer 에 더하고, 하위 탐색
#     if len(right_in)>0:
#         answer.append(right_root)
#         if len(_post) == 2:
#             process(right_root, right_in, [_post[0]])
#         else:
#             process(right_root, right_in, _post[bound_idx:len(_post)-1])

# process(_post[-1], _in, _post)

# print(' '.join(list(map(str,answer))))



''' 2트 => 답 참고
'''
import sys
sys.setrecursionlimit(10**9)

n = int(input())

_in = list(map(int,input().split()))
_post = list(map(int,input().split()))

answer = []

def process(in_start, in_end, post_start, post_end):
    global answer

    if (in_start > in_end) or (post_start > post_end): return

    # post order 에서 root 찾기
    root = _post[post_end]
    answer.append(root)

    # in order 에서 root 를 기준으로 left, right 나누기
    left = in_pos[root] - in_start
    right = in_end - in_pos[root]

    # 왼쪽 트리 탐색
    process(in_start, in_start+left-1, post_start, post_start+left-1)
    # 오른쪽 트리 탐색
    process(in_end-right+1, in_end, post_end-right, post_end-1)

in_pos = [0] * (n+1)
for i in range(n):
    in_pos[_in[i]] = i

process(0,n-1,0,n-1)

print(' '.join(list(map(str,answer))))
