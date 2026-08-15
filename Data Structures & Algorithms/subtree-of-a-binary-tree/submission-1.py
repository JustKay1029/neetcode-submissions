class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        # 1. Check if the trees match starting from the current root node
        if self.isSameTree(root, subRoot):
            return True
        
        # 2. Otherwise, recursively check the left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both are null -> identical
        if not p and not q:
            return True
        # One is null or values don't match -> not identical
        if not p or not q or p.val != q.val:
            return False
        
        # Check both left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)