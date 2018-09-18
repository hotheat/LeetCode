class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ix = -2
        max_tmp = float('-inf')
        for i, v in enumerate(nums):
            max_tmp = max(max_tmp, v)
            if v < max_tmp:
                max_ix = i

        min_ix = -1
        min_tmp = float('inf')
        for i in range(len(nums))[::-1]:
            min_tmp = min(min_tmp, nums[i])
            if nums[i] > min_tmp:
                min_ix = i
        return max_ix - min_ix + 1


arr = [1, 2, 3, 4]
# arr = [1, 3, 2, 2, 2]
s = Solution()
print(s.findUnsortedSubarray(arr))
