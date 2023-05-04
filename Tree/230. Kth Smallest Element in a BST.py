from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node: Optional[TreeNode], k):
            if not node:
                k -= 1
                return True
            if node:
                dfs(node.left, k)

        return dfs(root, k)
