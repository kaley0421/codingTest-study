import sys
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())

graph = dict()
for _ in range(n+m):
    a,b,c = input().split()
    if a in graph:
        graph[a].append((b,c))
    else:
        graph[a] = [(b,c)]

def dfs(start):
    global files, cnt

    if start in graph:
        for name,isFolder in graph[start]:
            if isFolder == '1':
                dfs(name)
            else:
                files.add(name)
                cnt += 1

q = int(input())
files = set()
cnt = 0
for _ in range(q):
    dirs = input().split("/")
    files = set()
    cnt = 0
    dfs(dirs[-1])
    print(len(files), cnt)