# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def invertTree(self, root: 'TreeNode') -> 'TreeNode':
        d = deque([root])
        while d:
            tmp = d.popleft()
            if tmp:
                tmp.left, tmp.right = tmp.right, tmp.left
                d.append(tmp.left)
                d.append(tmp.right)
        return root