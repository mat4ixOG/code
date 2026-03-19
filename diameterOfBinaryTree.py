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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def calcHeight(node):
            if not node:
                return 0 
            
            left_height = calcHeight(node.left)
            right_height = calcHeight(node.right)
            
            self.res  = max (self.res , left_height + right_height)
            
            return 1 + max(left_height , right_height)
        
        calcHeight(root)
        return self.res

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    print(solution.diameterOfBinaryTree(root))  # Expected: 3