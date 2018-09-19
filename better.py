class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # 求列表累加和
        cumsum = [0]
        for i in nums:
            cumsum.append(cumsum[-1] + i)
        res = max(cumsum[i] - cumsum[i-k] for i in range(k, len(cumsum)))
        return res / k


nums = [1, 12, -5, -6, 50, 3]
k = 4
s = Solution()
print(s.findMaxAverage(nums, k))
