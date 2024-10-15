# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        point = result

        tmp = 0
        while head:
            # print(tmp, head.val, point)
            if head.val == 0:
                result.val = tmp
                if head.next is not None:
                    result.next = ListNode()
                result = result.next
                tmp = 0
            else:
                tmp += head.val

            
            head = head.next

        return point.next
