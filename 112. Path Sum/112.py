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
        queue = deque([(root, root.val)])
        while queue:
            node, s = queue.pop()
            # 判断叶节点
            if s == sum and node.left is None and node.right is None:
                return True
            if node.left:
                queue.append((node.left, s + node.left.val))
            if node.right:
                queue.append((node.right, s + node.right.val))
        return False
