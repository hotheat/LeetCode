class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        else:
            return n // 5 + self.trailingZeroes(n // 5)


n = 25
print(Solution().trailingZeroes(n))
