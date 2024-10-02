from collections import deque
def printboard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end="\t")
        print()
    print()

def solution(maps):
    answer = 0
    
    tovisit = deque()
    visited_board = [[float("inf") for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited_board[0][0] = 1
    
    tovisit.append([0, 0, 1])
    while tovisit:
        y, x, currcnt = tovisit.popleft()
        
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx] == 1 and visited_board[ny][nx] > currcnt+1:
                tovisit.append([ny, nx, currcnt+1])
                visited_board[ny][nx] = currcnt+1
              
        # print(y, x, currcnt)
        # printboard(visited_board)
                
    if visited_board[-1][-1] == float("inf"):
        return -1
        
    
    return visited_board[-1][-1]
