from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())
    # records[문제 번호] = {팀 아이디1 : [점수, 횟수, 시간], ...}
    records = dict()
    for i in range(1, k+1):
        records[i] = dict()
        for j in range(1, n+1):
            records[i][j] = [-1, 0, 0]

    
    for time in range(m):
        id, qnum, score = map(int, input().split())

        if qnum not in records or id not in records[qnum]:
            records[qnum][id] = [score, 1, time]
        elif records[qnum][id][0] < score:
            records[qnum][id] = [score, records[qnum][id][1]+1, time]
        else:
            records[qnum][id][1] += 1
            records[qnum][id][2] = time
        # print(id, qnum, score, dict(records))

    for i in range(1, k+1):
        for j in range(1, n+1):
            if records[i][j][0] == -1:
                records[i][j][0] = 0

    sumcords = defaultdict(list)
    for qnum in range(1, k+1):
        for id in range(1, n+1):
            if id not in sumcords.keys():
                sumcords[id] = records[qnum][id]
            else:
                sumcords[id] = [sumcords[id][0] + records[qnum][id][0], sumcords[id][1] + records[qnum][id][1], max(sumcords[id][2], records[qnum][id][2])]

    sortedlist = sorted(sumcords.items(), key=lambda k:(-k[1][0], k[1][1], k[1][2]))
    # print(sortedlist)

    for i in range(n):
        if i>0 and sortedlist[i-1][1] == sortedlist[i][1]:
            print(i)
        elif sortedlist[i][0] == t:
            print(i+1)
            break
