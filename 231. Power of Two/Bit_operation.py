class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n - 1))


for i in [1, 8, 20]:
    print(i)
    print(Solution().isPowerOfTwo(i))
