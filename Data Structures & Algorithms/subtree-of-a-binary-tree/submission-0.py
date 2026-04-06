class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool: 
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False

            if p.val != q.val:
                return False

            left = isSameTree(p.left, q.left)
            right = isSameTree(p.right, q.right)

            return left and right

        if not root:
            return False
        
        res = isSameTree(root, subRoot)
        
        return res or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)