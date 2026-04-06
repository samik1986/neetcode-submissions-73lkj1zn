
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        
        print(leftDepth, root.left, rightDepth, root.right)

        depth = 1 + max(leftDepth, rightDepth)

        return depth


