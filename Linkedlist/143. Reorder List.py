from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        tempHead = head
        l = tempHead
        r = tempHead.next
        while tempHead.next:
            while r.next:
                l = r
                r = r.next
            #head.next = None  
            newHead = tempHead.next
            r.next = newHead
            tempHead.next = r
            tempHead = r.next
            l.next = None
            
            l = tempHead
            r = tempHead.next

        while head:
            print(head.val)
            head = head.next

# [ 1, 2, 3, 4, 5]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

S = Solution()
S.reorderList(head)
