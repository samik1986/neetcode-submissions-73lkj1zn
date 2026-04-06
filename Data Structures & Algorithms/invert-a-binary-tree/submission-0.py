
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        old_left = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(old_left)
        
        return root