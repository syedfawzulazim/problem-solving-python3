class ListNode:
    def __init__(self, k = 0, x=0):
        self.prev = None
        self.key = k
        self.val = x
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
    def get(self, key: int) -> int:

    def remove(self, key):
    
    def insert(self, key, value):
        
       
    def put(self, key: int, value: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = value
         
      

        
# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
print(obj.get(2))
obj.put(2,6)
print(obj.get(1))
obj.put(1,5)
obj.put(1,2)
print(obj.get(1))
print(obj.get(2))
# obj.put(3,3)
# print(obj.get(2))
# obj.put(4,4)
