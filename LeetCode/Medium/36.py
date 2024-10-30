class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # valid row
        for i in range(len(board)):
            if len(set(board[i])) != len(board[i]) - board[i].count(".") + 1:
                return False

        # valid col
        for i in range(len(board)):
            numset = set()
            countdot = 0
            for j in range(len(board[i])):
                if board[j][i].isnumeric() and board[j][i] in numset:
                    return False
                elif board[j][i].isnumeric():
                    numset.add(board[j][i])
                else:
                    countdot += 1

            if countdot + len(numset) == len(board[i]):
                numset = set()
                countdot = 0
                continue
            else:
                return False

        # valid box
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                numset = set()
                dotcnt = 0
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l].isnumeric() and board[i+k][j+l] in numset:
                            return False
                        elif board[i+k][j+l].isnumeric():
                            numset.add(board[i+k][j+l])
                        else:
                            dotcnt += 1
                
                if len(numset)+dotcnt != 9:
                    return False
                else:
                    numset = set()
                    dotcnt = 0

        return True
                    



        
