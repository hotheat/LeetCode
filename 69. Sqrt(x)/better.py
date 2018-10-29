class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low, high = 0, x
        if x == 1:
            return 1
        while low <= high:
            ans = (low + high) // 2
            # print(low, high, ans)
            if ans ** 2 <= x < (ans + 1) ** 2:
                return ans
            elif ans ** 2 > x:
                high = ans
            else:
                low = ans
        return ans


for i in [0, 1, 4, 8, 9, 15, 16]:
    print(Solution().mySqrt(i))
