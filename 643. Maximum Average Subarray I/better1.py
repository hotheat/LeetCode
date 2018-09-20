class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_t = sum(nums[:k])
        temp = max_t
        for i in range(len(nums) - k):
            temp = temp - nums[i] + nums[i + k]
            if temp > max_t:
                max_t = temp
        return max_t / k


nums = [1, 12, -5, -6, 50, 3]
k = 4
s = Solution()
print(s.findMaxAverage(nums, k))
