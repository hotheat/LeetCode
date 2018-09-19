class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_tmp, max_tmp = float('inf'), float('-inf')
        beg, end = -1, -2
        for i in range(len(nums)):
            max_tmp = max(nums[i], max_tmp)
            if nums[i] < max_tmp:
                end = i
            min_tmp = min(min_tmp, nums[len(nums) - 1 - i])
            if nums[len(nums) - 1 - i] > min_tmp:
                beg = len(nums) - 1 - i
        return end - beg + 1


# arr = [1, 2, 3, 4]
arr = [1, 3, 2, 2, 2]
s = Solution()
print(s.findUnsortedSubarray(arr))
