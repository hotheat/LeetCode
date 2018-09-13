class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i + 1]:
                return True
        return False


arr = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
s = Solution()
print(s.containsDuplicate(arr))
