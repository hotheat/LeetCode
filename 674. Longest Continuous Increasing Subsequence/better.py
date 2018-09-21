class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        anchor = 0
        i = 0
        while i < len(nums):
            if i > 0 and nums[i - 1] >= nums[i]:
                anchor = i
            else:
                res = max(res, i - anchor + 1)
            i += 1
            print(anchor, res)
        return res


nums = [1, 2, 4, 3]
s = Solution()
print(s.findLengthOfLCIS(nums))
