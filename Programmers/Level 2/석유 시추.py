import sys
sys.setrecursionlimit(10**7)

def DFS(y, x, nchar, maxh, maxw, board):
    global rsize
    rsize += 1
    
    if y-1 >= 0 and board[y-1][x] == 1:
        board[y-1][x] = nchar
        DFS(y-1, x, nchar, maxh, maxw, board)
        
    if x-1 >= 0 and board[y][x-1] == 1:
        board[y][x-1] = nchar
        DFS(y, x-1, nchar, maxh, maxw, board)
        
    if y+1 < maxh and board[y+1][x] == 1:
        board[y+1][x] = nchar
        DFS(y+1, x, nchar, maxh, maxw, board)
        
    if x+1 < maxw and board[y][x+1] == 1:
        board[y][x+1] = nchar
        DFS(y, x+1, nchar, maxh, maxw, board)
    
    return rsize
    
    

def solution(land):
    global rsize
    rsize = 0
    answer = 0

    diggingsize = dict()
    
    maxheight = len(land)
    maxwidth = len(land[0])
    
    currhole = 'A'
    
    for w in range(maxheight):
        for h in range(maxwidth):
            if land[w][h] == 1:
                land[w][h] = currhole
                rsize = DFS(w, h, currhole, maxheight, maxwidth, land)
                diggingsize[currhole] = rsize
                currhole = chr(ord(currhole)+1)
                rsize = 0
    
    tmpcalc = 0
    visited = set()
    for i in range(maxwidth):
        for j in range(maxheight):
            if land[j][i] in diggingsize.keys() and land[j][i] not in visited:
                visited.add(land[j][i])
                tmpcalc += diggingsize[land[j][i]]
        answer = max(tmpcalc, answer)
        tmpcalc = 0
        visited = set()
    
    return answer
