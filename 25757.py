import sys
input = sys.stdin.readline

N, game = map(str, input().split())
N = int(N)

players = set()

for _ in range(N):
    players.add(input())


if game == 'Y':
    print(len(players))
elif game == 'F':
    print(len(players)//2)
elif game == 'O':
    print(len(players)//3)
