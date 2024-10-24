# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = head
        while front != None and front.next != None:
            newnode = ListNode(gcd(front.val, front.next.val))
            newnode.next = front.next
            front.next = newnode
            # print(newnode.val, newnode.next.val)

            front = front.next.next

        return head
