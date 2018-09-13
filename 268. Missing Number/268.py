class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] == 1:
                return 0
            if nums[0] == 0:
                return 1

        nums.sort()
        for i, v in enumerate(nums):
            if v != i:
                return i
        return nums[-1] + 1


arr = [2, 1, 3]
s = Solution()
print(s.missingNumber(arr))
