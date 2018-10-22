class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        r = 1
        while x / r >= 10:
            r *= 10

        while r > 1:
            left, x = divmod(x, r)
            x, right = divmod(x, 10)

            if left != right:
                return False
            # 每次去除头尾两个元素，所以要除以 100
            r /= 100
        return True


x = 10
print(Solution().isPalindrome(x))
