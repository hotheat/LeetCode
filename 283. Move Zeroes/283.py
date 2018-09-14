class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while j < len(nums):
            if nums[i] == 0:
                t = nums.pop(i)
                nums.append(t)
            else:
                i += 1
            j += 1


nums = [1, 0, 0, 3, 12]
s = Solution()
s.moveZeroes(nums)
print(nums)
