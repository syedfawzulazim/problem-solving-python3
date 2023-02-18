from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap = {}
        curr = head
        while curr:
            if curr in hashmap:
                return True
            hashmap[curr] = curr.val
            curr = curr.next
        return False





head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)

S = Solution()
print(S.hasCycle(head))