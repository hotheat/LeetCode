class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # 求和也可以利用高斯求和公式
        s = int((n + 1) * n / 2)
        # s = sum(range(n))
        return s - sum(nums)


arr = [2, 0, 3]
s = Solution()
print(s.missingNumber(arr))
