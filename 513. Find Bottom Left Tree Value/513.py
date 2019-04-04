from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        pre = level = 1
        res = root
        d = deque([(root, level)])
        while len(d) > 0:
            n, l = d.popleft()
            if l > pre:
                res = n
            if n.left is not None:
                d.append((n.left, l + 1))
            if n.right is not None:
                d.append((n.right, l + 1))
            pre = l

        return res.val
