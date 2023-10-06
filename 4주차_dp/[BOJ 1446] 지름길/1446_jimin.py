n,d = map(int,input().split())

graph = [dict() for _ in range(d+1)]
for _ in range(n):
    start,end,dist = map(int,input().split())
    if 0<=start<=d and 0<=end<=d:
        if end not in graph[start]: graph[start][end] = dist
        else: graph[start][end] = min(graph[start][end],dist)

dp = [i for i in range(d+1)]
for i in range(d+1):
    for j in range(i):
        if i in graph[j]:
            dp[i] = min(dp[i],dp[j]+graph[j][i])
        dp[i] = min(dp[i],dp[j]+(i-j))

print(dp[d])