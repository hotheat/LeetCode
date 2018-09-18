class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)
