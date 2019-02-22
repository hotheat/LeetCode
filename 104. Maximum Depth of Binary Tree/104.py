# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def maxDepth(self, root: 'TreeNode') -> 'int':
        if root is not None:
            level = 1
            qeque = deque([(root, level)])
            while qeque:
                t, l = qeque.popleft()
                level = l + 1
                if t.left:
                    qeque.append((t.left, level))
                if t.right:
                    qeque.append((t.right, level))
            return l
        else:
            return 0
