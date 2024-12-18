from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or  len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedArr = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i+1 < len(lists) else None
                mergedArr.append(self.mergedList(l1,l2))
            lists= mergedArr
        return lists[0]
    
    def mergedList(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if not l1:
            tail.next = l2
        if not l2:
            tail.next = l1

        return dummy.next




list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

S =  Solution()
result = S.mergeKLists([list1, list2, list3])

# Print the result list
while result:
    print(result.val, end=" ")
    result = result.next



import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
	
# def mergeKLists_heapq( lists):
# 	h = []
# 	head = tail = ListNode(0)
# 	for i in range(len(lists)):
# 		heapq.heappush(h, (lists[i].val, i, lists[i]))

# 	while h:
# 		node = heapq.heappop(h)
# 		node = node[2]
# 		tail.next = node
# 		tail = tail.next
# 		if node.next:
# 			i+=1
# 			heapq.heappush(h, (node.next.val, i, node.next))

# 	return head.next


# list1 = ListNode(1, ListNode(4, ListNode(5)))
# list2 = ListNode(1, ListNode(3, ListNode(4)))
# list3 = ListNode(2, ListNode(6))


# result = mergeKLists_heapq([list1, list2, list3])

# # Print the result list
# while result:
#     print(result.val, end=" ")
#     result = result.next
