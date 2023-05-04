from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        res = newList
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum = v1 + v2 + carry
            carry = sum // 10
            reminder = sum % 10

            res.next = ListNode(reminder)

            res = res.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
       
        return newList.next


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
