import sys
sys.setrecursionlimit(10**7)

def DFS(y, x, board, result):
    global visited
    
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    for i in range(4):
        newy = dy[i]
        newx = dx[i]

        if 0 <= y+newy < len(board) and 0 <= x+newx < len(board[0]) and board[y+newy][x+newx] != 'X' and (y+newy, x+newx) not in visited:
            visited.add((y+newy, x+newx))
            result = DFS(y+newy, x+newx, board, result+int(board[y+newy][x+newx]))

    return result


def solution(maps):
    global visited
    answer = []

    visited = set()

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and (i, j) not in visited:
                visited.add((i, j))
                answer.append(DFS(i, j, maps, int(maps[i][j])))

    answer.sort()
    if len(answer) == 0:
        return [-1]

    return answer
