class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        number = dict(zip(range(0, 26), [chr(i) for i in range(65, 91)]))

        ans = ''

        while True:
            div, mod = divmod(n - 1, 26)
            ans = number[mod] + ans
            if div == 0:
                break
            n = div
        return ans


n = 53
print(Solution().convertToTitle(n))
