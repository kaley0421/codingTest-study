''' 1트 => 시간 초과
'''
# t = int(input())

# def find(parent,x):
#     if parent[x] != x:
#         parent[x] = find(parent,parent[x])
#     return parent[x]

# def union(parent,a,b):
#     a = find(parent,a)
#     b = find(parent,b)
#     if a < b: parent[b] = a
#     else: parent[a] = b

# for _ in range(t):
#     name_dict = dict()
#     f = int(input())
#     parent = []

#     for _ in range(f):
#         p1,p2 = input().split()
#         if p1 not in name_dict.keys():
#             name_dict[p1] = len(name_dict.keys())
#             parent.append(len(parent))
#         if p2 not in name_dict.keys():
#             name_dict[p2] = len(name_dict.keys())
#             parent.append(len(parent))
#         union(parent, name_dict[p1], name_dict[p2])
#         root = find(parent, name_dict[p1])
#         cnt = 0
#         for i in range(len(parent)):
#             if parent[i] == root: cnt += 1
#             elif find(parent,i) == root: cnt += 1
#         print(cnt)



''' 2트 => 답 참고
1. child_cnt 에 해당 노드의 자식 수를 저장 -> root 에 연결되어 있는 사람 수를 세어 나간다.
2. union 함수 내부에서 (a 의 루트 != b 의 루트) 일 경우,
    -> b 의 루트를 a 의 루트로 설정
    -> a 의 자식 수에 b 의 자식 수를 더해준다.
'''
t = int(input())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        child_cnt[a] += child_cnt[b]

for _ in range(t):
    f = int(input())
    parent = dict()
    child_cnt = dict()

    for _ in range(f):
        p1,p2 = input().split()

        if p1 not in parent:
            parent[p1] = p1
            child_cnt[p1] = 1
        if p2 not in parent:
            parent[p2] = p2
            child_cnt[p2] = 1
        
        union(p1,p2)
        root = find(p1)
        print(child_cnt[root])
        