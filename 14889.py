from sys import stdin
from itertools import combinations
input = stdin.readline

N = int(input())
strgths = []

for _ in range(N):
    strgths.append(list(map(int, input().split())))

players = {i for i in range(N)}

combs = list(combinations(players, N//2))

result = float("inf")

for comb in combs:
    team1 = list(comb)
    team2 = list(players - set(comb))

    com1 = list(combinations(team1, 2))
    tmpstr1 = 0
    for c1, c2 in com1:
        tmpstr1 += strgths[c1][c2] + strgths[c2][c1]

    com2 = list(combinations(team2, 2))
    tmpstr2 = 0
    for c1, c2 in com2:
        tmpstr2 += strgths[c1][c2] + strgths[c2][c1]

    result = min(result, abs(tmpstr1-tmpstr2))

    # print(tmpstr1, tmpstr2, maxstr1, maxstr2)
    
print(result)

