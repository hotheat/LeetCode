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
        d = deque([root])
        while len(d) > 0:
            n = d.popleft()
            if n.right is not None:
                d.append(n.right)
            if n.left is not None:
                d.append(n.left)

        return n.val