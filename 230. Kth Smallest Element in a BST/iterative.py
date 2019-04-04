# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        self.k = k
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            self.k -= 1
            if self.k == 0:
                return root.val
            root = root.right
        return None