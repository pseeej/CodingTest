import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

board = []
for _ in range(5):
    board.append(list(map(int, input().split())))

patterns = set()
def DFS(y, x, code):
    global patterns

    if len(code) == 6:
        if code not in patterns:
            patterns.add(code)

        return
    
    if y > 0:
        DFS(y-1, x, code + str(board[y-1][x]))
    if x > 0:
        DFS(y, x-1, code + str(board[y][x-1]))
    if y < 5-1:
        DFS(y+1, x, code + str(board[y+1][x]))
    if x < 5-1:
        DFS(y, x+1, code + str(board[y][x+1]))

for i in range(5):
    for j in range(5):
        DFS(i, j, "")
print(len(patterns))
