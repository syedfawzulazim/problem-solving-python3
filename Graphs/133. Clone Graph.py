from collections import deque
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}

        def bfs(node: Node):
            q = deque()
            q.append(node)

            while q: 
                n: Node = q.popleft()
                if n.val not in visited.keys():
                    visited[n.val] = Node(n.val)
                for x in n.neighbors:
                    if x.val not in visited.keys():
                        q.append(x)
                    else:
                        if visited[x.val] not in visited[n.val].neighbors:
                            visited[n.val].neighbors.append(visited[x.val])
                        if visited[n.val] not in visited[x.val].neighbors:
                            visited[x.val].neighbors.append(visited[n.val])

        bfs(node)

        print(visited)



# Create a graph
node1 = Node(1, [])
node2 = Node(2, [])
node3 = Node(3, [])
node4 = Node(4, [])

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

# Clone the graph
solution = Solution()
cloned_node = solution.cloneGraph(node1)

# Print the cloned graph
# print(cloned_node.val)   # 1
# print([n.val for n in cloned_node.neighbors])   # [2, 4]
