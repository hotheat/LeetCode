import math


class Solution:
    def numSquares(self, n: int) -> int:
        """
        借用第一种动态规划的思路
        如果一个完美平方数加上某个数恰好等于当前数，那只需要在当前的计数上加 1 即可
        和硬币找零类似
        https://www.youtube.com/watch?v=BT7qmMpUBKE
        :param n:
        :return:
        """
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = 1
            min_value = float('inf')
            while j * j <= i:
                min_value = min(min_value, dp[i - j * j] + 1)
                j += 1
            dp[i] = min_value
        return dp[-1]


if __name__ == '__main__':
    n = 13
    print(Solution().numSquares(n))
