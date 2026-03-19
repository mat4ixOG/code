from typing import Optional

from balancedBinaryTree import TreeNode


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
        
        if not root:
            return False
        
        if isSameTree(root, subRoot):
            return False
        
        return self.isSubtree(root.___, subRoot) or \
               self.isSubtree(root.___, subRoot)