from collections import deque


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self.helper(None, root, None)

    def helper(self, minv, root, maxv):
        if root is None:
            return True

        if (minv is not None and root.val < minv) or (maxv is not None and root.val > maxv):
            return False

        left = self.helper(minv, root.left, root.val - 1)
        right = self.helper(root.val + 1, root.right, maxv)
        return left and right