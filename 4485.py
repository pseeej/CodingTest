from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
T = 0
while N != 0:
    T += 1

    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    visited = [[float("inf") for _ in range(N)] for _ in range(N)]
    # print(visited)
    visited[0][0] = board[0][0]

    # 최단거리는 보통 BFS니깐...
    tovisit = deque()
    tovisit.append((0, 0, board[0][0]))

    while tovisit:
        cury, curx, nowcost = tovisit.popleft()

        if nowcost > visited[cury][curx]:
            continue

        if cury-1 >= 0 and visited[cury-1][curx] > board[cury-1][curx]+nowcost:
            visited[cury-1][curx] = board[cury-1][curx]+nowcost
            tovisit.append((cury-1, curx, visited[cury-1][curx]))
        if curx-1 >= 0 and visited[cury][curx-1] > board[cury][curx-1]+nowcost:
            visited[cury][curx-1] = board[cury][curx-1]+nowcost
            tovisit.append((cury, curx-1, visited[cury][curx-1]))
        if cury+1 < N and visited[cury+1][curx] > board[cury+1][curx]+nowcost:
            visited[cury+1][curx] = board[cury+1][curx]+nowcost
            tovisit.append((cury+1, curx, visited[cury+1][curx]))
        if curx+1 < N and visited[cury][curx+1] > board[cury][curx+1]+nowcost:
            visited[cury][curx+1] = board[cury][curx+1]+nowcost
            tovisit.append((cury, curx+1, visited[cury][curx+1]))

    print(f"Problem {T}: {visited[N-1][N-1]}")

    N = int(input())
    
'''
    for i in range(N):
        for j in range(N):
            print(visited[i][j], end=" ")
        print()
'''
            
            
