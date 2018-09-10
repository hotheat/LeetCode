class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, v in enumerate(nums):
            other = target - v
            if other == v:
                if other in nums[i + 1:]:
                    return nums.index(v), nums.index(v) + nums[i + 1:].index(other) + 1
            elif other in nums:
                return nums.index(v), nums.index(other)
        return None


s = Solution()
nums = [3, 2, 4]
target = 6
print(s.twoSum(nums, target))
