from heapq import heappush, heappop
def printboard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end="\t")
        print()
    print()

def solution(maps):
    answer = 0
    maxval = 1000000
    
    R, C = len(maps), len(maps[0])
    
    for i in range(R):
        for j in range(C):
            if maps[i][j] == "S":
                startpoint = (i, j)
            elif maps[i][j] == "E":
                endpoint = (i, j)
            elif maps[i][j] == "L":
                leverpoint = (i, j)
                
                
    # startpoint -> leverpoint
    min_visited = [[maxval for _ in range(C)] for _ in range(R)]
    min_visited[startpoint[0]][startpoint[1]] = 0
    
    tovisit = []
    y, x = startpoint
    heappush(tovisit, [0, y, x])
    
    checkIfFound = False
    while tovisit:
        # print(tovisit)
        # printboard(min_visited)
        currcnt, y, x = heappop(tovisit)
        
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if 0 <= ny < R and 0 <= nx < C and maps[ny][nx] != 'X' and min_visited[ny][nx] > currcnt+1:
                # print(ny, nx)
                min_visited[ny][nx] = currcnt+1
                
                if (ny, nx) == leverpoint:
                    checkIfFound = True
                    break
                else:
                    heappush(tovisit, [currcnt+1, ny, nx])
        
        if checkIfFound:
            break
                    
    minlever = min_visited[leverpoint[0]][leverpoint[1]]
    printboard(min_visited)
    
    
    # leverpoint -> endpoint
    min_visited = [[maxval for _ in range(C)] for _ in range(R)]
    min_visited[leverpoint[0]][leverpoint[1]] = minlever
    
    tovisit = []
    y, x = leverpoint
    heappush(tovisit, [minlever, y, x])
    
    checkIfFound = False
    while tovisit:
        # print(tovisit)
        # printboard(min_visited)
        currcnt, y, x = heappop(tovisit)
        
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if 0 <= ny < R and 0 <= nx < C and maps[ny][nx] != 'X' and min_visited[ny][nx] > currcnt+1:
                # print(ny, nx)
                min_visited[ny][nx] = currcnt+1
                
                if (ny, nx) == endpoint:
                    checkIfFound = True
                    break
                else:
                    heappush(tovisit, [currcnt+1, ny, nx])
        
        if checkIfFound:
            break        
    
    if min_visited[endpoint[0]][endpoint[1]] != maxval:
        return min_visited[endpoint[0]][endpoint[1]]
    else:
        return -1
            
