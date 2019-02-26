class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if root.left is None and root.right is None:
            return root.val == sum
        new_sum = sum - root.val
        return self.hasPathSum(root.left, new_sum) or self.hasPathSum(root.right, new_sum)
