import sys
input = sys.stdin.readline

N, D = map(int, input().split())
road = [i for i in range(D+1)]
shortlist = []

for _ in range(N):
    start, end, cost = map(int, input().split())
    shortlist.append([start, end, cost])

shortlist.sort()
for short in shortlist:
    start, end, cost = short[0], short[1], short[2]
    for i in range(end, D+1):
        # if i == end and road[i] > road[start]+cost:
            # print(i, road[i], road[start]+cost+(i-end))
        road[i] = min(road[i], road[start]+cost+(i-end))

print(road[-1])
