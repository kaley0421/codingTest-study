from itertools import combinations

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

start_teams = list(combinations([i for i in range(n)],n//2))

answer = 1e9
for start_team in start_teams:
    link_team = []
    for x in range(n):
        if x not in start_team: link_team.append(x)

    start_score = 0
    for i in range(len(start_team)):
        for j in range(len(start_team)): start_score += graph[start_team[i]][start_team[j]]
    
    link_score = 0
    for i in range(len(link_team)):
        for j in range(len(link_team)): link_score += graph[link_team[i]][link_team[j]]
    
    answer = min(answer, abs(start_score-link_score))
    if answer == 0: break

print(answer)    