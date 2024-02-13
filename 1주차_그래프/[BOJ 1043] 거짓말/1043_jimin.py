''' 1트 => 유니온 파인드 사용
'''
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a == truth_group:
        parent[b] = truth_group
    elif b == truth_group:
        parent[a] = truth_group
    elif a<b: 
        parent[b] = a
    else: 
        parent[a] = b

n,m = map(int,input().split())
parent = [i for i in range(n+1)]
answer = m
truth_group = -1

t = list(map(int,input().split()))
truth_cnt = t[0]
truth_people = t[1:]
if len(truth_people) > 1:
    for _t in truth_people:
        union(truth_people[0], _t)
if truth_people:
    truth_group = find(truth_people[0])

p = []
for i in range(m):
    p.append(list(map(int,input().split())))
    people_cnt = p[i][0]
    people = p[i][1:]
    if len(people) > 1:
        for _p in people:
            union(people[0], _p)

for i in range(m):
    people_cnt = p[i][0]
    people = p[i][1:]
    for _p in people:
        if find(_p) == truth_group:
            answer -= 1
            break

print(answer)


''' 2트 => 집합 사용. 실패.
[ 반례 ]
5 4
1 5
2 1 2
2 2 3
2 3 4
2 4 5
[ 집합으로 풀리지 않는 이유 ]
1. 위 반례에서 5-4-3-2-1 이 모두 연결되어 있다는 정보를 찾지 못한다.
2. 단순히 '진실을 알고 있는 사람들의 집합' 을 set()에 넣어 관리하는 것이 아니라, '사람들 간의 연결 정보' 를 관리해야 함
    -> 분리집합 사용
'''
n,m = map(int,input().split())
answer = m
truth_group = set()

t = list(map(int,input().split()))
truth_cnt = t[0]
truth_people = t[1:]
for _t in truth_people:
    truth_group.add(_t)

p = []
for i in range(m):
    p.append(list(map(int,input().split())))
    people_cnt = p[i][0]
    people = p[i][1:]
    for _p in people:
        if _p in truth_group:
            for __p in people:
                truth_group.add(__p)
            break

for i in range(m):
    people_cnt = p[i][0]
    people = p[i][1:]
    for _p in people:
        if _p in truth_group:
            answer -= 1
            break

print(answer)