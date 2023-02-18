from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l, r = head, head
        
        if head.next == None and n == 1:
            head.val = None

        m = 1
        while m < n:
            r = r.next
            m += 1
        prev = ListNode()
        while r.next:
            prev = l
            l = l.next
            r = r.next
    
        prev.next = l.next  
        
       




# [1,2,3,4,5]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

S =  Solution()
S.removeNthFromEnd(head, 2)
while head:
    print(head.val)
    head = head.next