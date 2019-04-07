class Solution:
    def numSquares(self, n: int) -> int:
        """
        动态规划（1）和找硬币思路类似
        数组 dp[i] 代表当硬币面额为 i 时所需的最小平方和数
        先将完全平方数填充，dp[i] 的最小平方数可以由和等于 i 的两个数 dp[j] + dp[i-j] 的
        最小平方数加和构成.
        但是这种方法会造成 Time limit exceeded
        :param n:
        :return:
        """
        dp = [float('inf')] * (n + 1)
        # 初始化
        for i in range(1, n + 1):
            if i ** 2 <= n:
                dp[i ** 2] = 1

        for i in range(1, n + 1):
            for j in range(1, i // 2 + 1):
                dp[i] = min(dp[j] + dp[i - j], dp[i])

        return dp[-1]


if __name__ == '__main__':
    num = 13
    print(Solution().numSquares(num))
