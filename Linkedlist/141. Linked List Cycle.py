from typing import Optional


class ListNode:
    def __init__(self, x, y = None):
        self.val = x
        self.next = y

class Solution:
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     hashmap = {}
    #     curr = head
    #     while curr:
    #         if curr in hashmap:
    #             return True
    #         hashmap[curr] = curr.val
    #         curr = curr.next
    #     return False
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next

        while head and fast:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next if fast.next else None
            head = head.next
        return False



head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)

S = Solution()
print(S.hasCycle(head))