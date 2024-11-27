# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        board = [[-1 for _ in range(n)] for _ in range(m)]
        
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        y, x = 0, 0
        currdir = 0

        board[y][x] = head.val
        head = head.next

        while head:
            num = head.val
            dy, dx = d[currdir]
            ny, nx = y+dy, x+dx

            while not(0 <= ny < m and 0 <= nx < n and board[ny][nx] == -1):
                currdir = (currdir+1)%4
                dy, dx = d[currdir]
                ny, nx = y+dy, x+dx

            board[ny][nx] = num
            
            y, x = ny, nx
            head = head.next





        return board
        
