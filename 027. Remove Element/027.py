class Solution:
    def removeElement(self, nums, val):
        """
        Given nums = [3,2,2,3], val = 3,
        return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i, j = 0, 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            else:
                continue
        return j


s = Solution()
nums = []
val = 2
print(s.removeElement(nums, val))
