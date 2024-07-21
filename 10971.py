import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

tempres = []
def recur(curr, visited, dists):
    # print(curr, visited, dists)
    if len(visited) == N and board[curr][visited[0]] != 0:
        tempres.append(dists+board[curr][visited[0]])
        return
    elif len(visited) == N:
        return
    if len(tempres) and dists > min(tempres):
        return
    
    for i in range(N):
        if i not in set(visited) and board[curr][i] != 0:
            newvisited = list(visited)
            newvisited.append(i)
            recur(i, newvisited, dists+board[curr][i])

    return dists

result = float("inf")
for num in range(N):
    recur(num, [num], 0)
    result = min(result, min(tempres))
    tempres = []

print(result)
