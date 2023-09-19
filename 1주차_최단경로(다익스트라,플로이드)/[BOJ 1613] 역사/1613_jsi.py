# 왜 시간 초과지?,, 함수 없애고 a와 b가 같을 경우가 없어서 [a][a] 0 초기화도 뺐는디
# 연결 유무만 보면 됨 -> INF 대신 boolean으로
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = True

def floyd():
    for v in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][v] and graph[v][j]:
                    graph[i][j] = True

floyd()

s = int(input())

for _ in range(s):
    a, b = map(int, input().split())

    if graph[a][b]:
        print(-1)
    elif graph[b][a]:
        print(1)
    else:
        print(0)