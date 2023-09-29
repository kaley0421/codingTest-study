import sys
from itertools import combinations

N = int(input())
graph = []
answer = 1e9

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

_comb = list(combinations([i for i in range(N)], N//2))
_comb = _comb[:len(_comb) // 2]

for team in _comb:
    _sum1, _sum2 = 0, 0

    for i in set(team):
        for j in set(team) - set([i]):
            _sum1 += graph[i][j]

    another_team = set([i for i in range(N)]) - set(team)
    for i in another_team:
        for j in set(another_team) - set([i]):
            _sum2 += graph[i][j]

    answer = min(answer, abs(_sum1 - _sum2))

print(answer)