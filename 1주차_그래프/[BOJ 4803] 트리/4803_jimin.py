'''
[ 사이클이 없는 연결 요소 (트리) 찾기 - 유니온 파인드 사용 ]
1. 사이클을 발견하면, 사이클의 루트 노드를 cycles 집합에 추가한다.
2. 그래프에서 트리들을 찾는다.
3. cycles 의 루트노드가 trees 에 존재한다면, 해당 root는 더이상 tree 가 아님 -> trees 에서 제외
    (ex. 노드 2,3,4 가 사이클을 이루고, 노드 1 이 2 와 연결되어 있는 경우)

[ BFS/DFS 사용 ]
https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-4803-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%8A%B8%EB%A6%AC-%EA%B3%A8%EB%93%9C-4-%ED%8A%B8%EB%A6%AC
'''
import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b: parent[b] = a
    else: parent[a] = b

parent = []
answer = 0
case = 1

while True:
    n,m = map(int,sys.stdin.readline().split())

    if n==0 and m==0: break

    parent = [i for i in range(n)]
    cycles = set()
    for _ in range(m):
        a,b = map(int,sys.stdin.readline().split())
        a -= 1
        b -= 1
        if find(a) == find(b):
            cycles.add(find(a))
        else:
            union(a,b)

    trees = set()
    for i in range(n):
        trees.add(find(i))

    # cycles 의 root 가 trees 에 속한다면, 해당 root 는 더이상 tree 가 아님 -> trees 에서 제외
    for c in list(cycles):
        if find(c) in trees:
            trees.remove(find(c))

    answer = len(trees-cycles)

    print("Case " + str(case) + ": ", end = "")
    if answer==0:
        print("No trees.")
    elif answer==1:
        print("There is one tree.")
    else:
        print("A forest of", answer, "trees.")
    
    case += 1