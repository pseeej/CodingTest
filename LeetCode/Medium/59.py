class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        board = [[0 for _ in range(n)] for _ in range(n)]

        y, x = 0, 0
        cnt = 1
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        turn = 0
        board[y][x] = cnt

        while True:
            cnt += 1
            dy, dx = d[turn]

            ny, nx = y+dy, x+dx
            if not (0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0):
                turn = (turn+1)%len(d)
                dy, dx = d[turn]
                ny, nx = y+dy, x+dx

            if not (0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0):
                break

            board[ny][nx] = cnt
            y, x = ny, nx

        return board
