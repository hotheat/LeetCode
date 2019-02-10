class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = -1 if x < 0 else 1
        x = x * s

        n = 0
        while x > 0:
            n = (n * 10) + (x % 10)
            x = x // 10

        if n > 0x7FFFFFFF:
            return 0

        return n * s


x = -1234
print(Solution().reverse(x))
