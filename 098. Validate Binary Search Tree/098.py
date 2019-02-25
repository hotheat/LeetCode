# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        if root:
            d = deque([(float('-inf'), root, float('inf'))])
            while d:
                minv, node, maxv = d.popleft()
                if minv > node.val or node.val > maxv:
                    return False
                if node.left:
                    d.append((minv, node.left, node.val - 1))
                if node.right:
                    d.append((node.val + 1, node.right, maxv))
            return True
        else:
            return True
