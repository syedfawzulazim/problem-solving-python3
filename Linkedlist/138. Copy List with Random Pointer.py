from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
        
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        hashmap = {}
        while curr:
            hashmap[curr] = Node(curr.val)
            curr = curr.next
        

        curr = head
        while curr:
            if curr.next:
                hashmap[curr].next = hashmap[curr.next]
            if curr.random:
                hashmap[curr].random = hashmap[curr.random]
            curr = curr.next
        return hashmap[head]


head = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head.random = None
node2.random = head
node3.random = node5
node4.random = node3
node5.random = head

# create an instance of the Solution class
sol = Solution()

# call the copyRandomList function
copy_head = sol.copyRandomList(head)

# print the original and copy linked lists
print("Original list:")
curr = head
while curr:
    print(f"val: {curr.val}, random: {curr.random.val if curr.random else None}")
    curr = curr.next

print("Copy list:")
curr = copy_head
while curr:
    print(f"val: {curr.val}, random: {curr.random.val if curr.random else None}")
    curr = curr.next