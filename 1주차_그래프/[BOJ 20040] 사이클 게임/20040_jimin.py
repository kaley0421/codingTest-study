'''
1. 사이클 발생 여부는 모든 간선에 대해 union, find 연산을 수행해 가며 판별한다.
    (어떤 한 간선을 노드 a,b 가 이룬다고 할 때)
    - <a 의 루트 == b 의 루트> 라면, 사이클 발생
    - <a 의 루트 != b 의 루트> 라면, union 연산
'''
import sys
n,m = map(int,input().split())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b: parent[b] = a
    else: parent[a] = b

parent = [i for i in range(n)]

for round in range(1,m+1):
    a,b = map(int, sys.stdin.readline().split())
    # 사이클 존재 여부 판별
    if find(a) == find(b):
        print(round)
        exit()
    else:
        union(a,b)

print(0)