class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ns = set(nums)
        n = len(nums) + 1
        for i in range(n):
            if i not in ns:
                return i
