from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        N1= l1
        N2= l2

        res = ListNode()
        curr = res
        carry = 0
        while N1 and N2:
            sum = N1.val + N2.val + carry
            carry = sum // 10
            rem = sum % 10 

            curr.next = ListNode(rem)
            curr = curr.next

            if N1.next and N2.next == None:
                N2.next = ListNode()
            elif N1.next == None and N2.next:
                N1.next = ListNode()

            N1 = N1.next
            N2 = N2.next
        if carry:
            curr.next = ListNode(carry)

        return res.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(6)

# 6342 + 465

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

S  = Solution()
res = S.addTwoNumbers(l1,l2)

curr = res
while curr:
    print(curr.val)
    curr = curr.next
