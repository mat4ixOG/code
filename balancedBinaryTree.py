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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left == -1 or right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1
            
            return 1 + max(left , right)
        
        return dfs(root) != -1

if __name__ == "__main__":
    # Test 1 - Expected: True
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # Test 2 - Expected: False
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    root2.left.left.left = TreeNode(6)

    solution = Solution()
    print(solution.isBalanced(root))   # True ✅
    print(solution.isBalanced(root2))  # False ✅