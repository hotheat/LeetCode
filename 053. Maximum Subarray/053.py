class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        # global_max 记录曾经遇到的最大值
        # current_max 记录指针所在位置的最大值
        gloal_max, current_max = nums[0], nums[0]
        for i in range(1, len(nums)):
            # 如果前面的所有值加和不如当前值大, 那么加和从当前值开始
            current_max = max(current_max + nums[i], nums[i])
            gloal_max = max(gloal_max, current_max)
        return gloal_max


s = Solution()
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(s.maxSubArray(arr))
