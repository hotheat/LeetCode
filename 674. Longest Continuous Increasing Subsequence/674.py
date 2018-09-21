class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []: return 0
        max_cnt = 1
        current_cnt = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                current_cnt += 1
            else:
                max_cnt = max(max_cnt, current_cnt)
                current_cnt = 1

        return max(max_cnt, current_cnt)


nums = [1, 3, 5, 4, 7]
s = Solution()
print(s.findLengthOfLCIS(nums))
