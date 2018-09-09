class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        if target < nums[0]:
            return 0
        while i < len(nums):
            if nums[i] == target:
                return i
            elif i < len(nums) - 1 and nums[i] < target < nums[i + 1]:
                return i + 1
            i += 1
        return i


s = Solution()
arr = [1, 3, 5, 6]
target = 4
print(s.searchInsert(arr, target))
