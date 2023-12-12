import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    teamnums = list(map(int, input().split()))

    team_members = defaultdict(list)

    for i in range(N):
        team_members[teamnums[i]].append(i)

    nocalc = set()
    for tm in team_members.keys():
        if len(team_members[tm]) < 6:
            nocalc.add(tm)

    team_scores = defaultdict(list)
    score = 1
    for i in range(N):
        if teamnums[i] not in nocalc:
            team_scores[teamnums[i]].append(score)
            score += 1

    for ts in team_scores.keys():
        team_scores[ts].sort()

    topscores = defaultdict(list)
    for ts in team_scores.keys():
        topscores[ts] = [sum(team_scores[ts][:4]), team_scores[ts][4]]

    # print(topscores)

    sortedteams = sorted(topscores.items(), key= lambda ts:(ts[1][0], ts[1][1]))

    # print(sortedteams)
    print(sortedteams[0][0])
    
