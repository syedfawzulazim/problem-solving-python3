from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy= ListNode(0, head)
        groupPrev = dummy

        while True:
            kth =  self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev = kth.next
            curr = groupPrev.next
            while curr != groupNext: # 0|1,2| 3,4,5 // 2,1, | 3,4,5
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            tmp = groupPrev.next # 1
            groupPrev.next = kth # dummy.next = 3 (previously head 1)
            groupPrev = tmp
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr




#1,2,3,4,5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


S = Solution()
print(S.reverseKGroup(head, 2))