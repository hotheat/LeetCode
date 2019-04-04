# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return [n for n in self.helper(root)]

    def helper(self, node):
        if node:
            yield node.val
            yield from self.helper(node.left)
            yield from self.helper(node.right)
