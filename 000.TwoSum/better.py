class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pair = {}
        for i, v in enumerate(nums):
            other = target - v
            if other in pair:
                return [pair[other], i]
            else:
                pair[v] = i


s = Solution()
nums = [3, 3, 4]
target = 6
print(s.twoSum(nums, target))
