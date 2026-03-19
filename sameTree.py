from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printTree(root):
    if not root:
        print([])
        return
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    print(result)


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left , q.left) and self.isSameTree(p.right , q.right)

if __name__ == "__main__":
    # Test 1 - Expected: True
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    # Test 2 - Expected: False
    p2 = TreeNode(1)
    p2.left = TreeNode(2)

    q2 = TreeNode(1)
    q2.right = TreeNode(2)

    solution = Solution()
    print(solution.isSameTree(p, q))   # True ✅
    print(solution.isSameTree(p2, q2)) # False ✅