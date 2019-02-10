class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low, high = 0, x
        ans = (low + high) / 2
        if x == 0:
            return 0
        while abs(ans ** 2 - x) > 0.01:
            if ans ** 2 < x:
                low = ans
            else:
                high = ans
            ans = (low + high) / 2
        return round(ans) if round(ans) == x else int(ans)


for i in [0, 1, 4, 8, 9, 15, 16]:
    print(Solution().mySqrt(i))
