from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

players = [i for i in range(N)]
result = float("inf")
for i in range(1, N//2+1):
    teams = list(combinations(players, i))

    for team in teams:
        ateam = tuple(set(players)-set(team))
        
        asum = 0
        for i in range(len(team)):
            for j in range(i+1, len(team)):
                asum += board[team[i]][team[j]]+board[team[j]][team[i]]

        bsum = 0
        for i in range(len(ateam)):
            for j in range(i+1, len(ateam)):
                bsum += board[ateam[i]][ateam[j]] + board[ateam[j]][ateam[i]]

        # print(team, ateam, asum, bsum)
        result= min(result, abs(asum-bsum))

print(result)

        
