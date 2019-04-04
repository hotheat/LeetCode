# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self.helper(root) != -1

    def helper(self, node):
        """
        helper 函数在求二叉树当前节点高度的基础上增加
        1. 判断当前子树是否是平衡二叉树
        2. 左右子节点高度差是否小于 1
        因为节点的高度都是正整数，所以是否是平衡二叉树可以用 -1 来代替
        :param node:
        :return:
        """
        if node is None:
            return 0

        left_depth = self.helper(node.left)
        right_depth = self.helper(node.right)
        if left_depth == -1 or right_depth == -1:
            return -1
        if abs(left_depth - right_depth) > 1:
            return -1
        return max(left_depth, right_depth) + 1
