# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        queue = deque([(root, sum-root.val)])
        while queue:
            node, v = queue.popleft()
            if v == 0 and node.left is None and node.right is None:
                return True
            if node.left:
                queue.append((node, v - node.left.val))
            if node.right:
                queue.append((node, v - node.right.val))
        return False