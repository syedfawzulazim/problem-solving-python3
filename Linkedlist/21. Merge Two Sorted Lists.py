from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        


head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)

head2 = ListNode(2)
head2.next = ListNode(3)
head2.next.next = ListNode(4)

s = Solution()
s.mergeTwoLists(head1, head2)
