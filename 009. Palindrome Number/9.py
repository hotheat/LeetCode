class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        i = 0
        while i < len(x) // 2:
            if x[i] != x[len(x) - (i + 1)]:
                return False
            i += 1
        return True


x = 121
print(Solution().isPalindrome(x))
