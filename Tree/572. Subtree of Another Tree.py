from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root, subRoot)
    def dfs(self, p, q):
        if p.val != q.val:
            self.dfs(p.left, q)
            self.dfs(p.right, q)
        else:
            self.dfs(p.left, q.left)
            self.dfs(p.right, q.right)
        
        
        




root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

s = Solution()
res = s.isSubtree(root, subRoot)
print(res)
