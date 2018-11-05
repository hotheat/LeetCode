class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1


for i in [1, 8, 20]:
    print(i)
    print(Solution().isPowerOfTwo(i))
