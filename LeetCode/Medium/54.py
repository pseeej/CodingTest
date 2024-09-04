class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        y, x = 0, 0
        turn = 0

        result.append(matrix[y][x])
        matrix[y][x] = 300

        checkIfDone = False

        while True:
            print(y, x)
            dy, dx = d[turn]
            orgturn = turn
            while not(0 <= y+dy < len(matrix) and 0 <= x+dx < len(matrix[0])) or matrix[y+dy][x+dx] == 300:
                turn = (turn+1)%len(d)
                if turn == orgturn:
                    checkIfDone = True
                    break
                dy, dx = d[turn]

            if checkIfDone:
                break

            result.append(matrix[y+dy][x+dx])
            y = y+dy
            x = x+dx
            matrix[y][x] = 300

        return result

            
