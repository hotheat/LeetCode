class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = None
        i = 0
        while i < len(nums):
            if pre is None:
                pre = nums[0]
                i += 1
            elif nums[i] == pre:
                pre = nums[i]
                nums.pop(i)
            else:   
                pre = nums[i]
                i += 1
        return len(nums)


nums = [1, 1, 2]
s = Solution()
print(s.removeDuplicates(nums))
