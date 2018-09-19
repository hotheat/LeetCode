class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) == 1: return nums[0]
        max_ave = float('-inf')
        for i in range(len(nums) - k + 1):
            max_ave = max(max_ave, sum(nums[i:i + k]) / k)
        return max_ave


nums = [1, 12, -5, -6, 50, 3]
k = 4
s = Solution()
print(s.findMaxAverage(nums, 4))
