from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recurrDepth(root, 0)
        
    def recurrDepth(self, root: Optional[TreeNode], n):
 
        if not root:
            n = n
            return
        else:
            n += 1
            self.recurrDepth(root.left, n)
            self.recurrDepth(root.right, n)
        return n



s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
inverted_root = s.maxDepth(root)
print(inverted_root)