class Solution:

    def integerBreak(self, n: int) -> int:
        """
        纯动态规划，时间复杂度 O(n^2)
        :param n:
        :return:
        """
        res = [1] * (n + 1)

        for i in range(3, n + 1):
            max_value = float('-inf')
            for j in range(1, i):
                max_value = max(j * res[i - j], j * (i - j), max_value)
            res[i] = max_value
        return res[-1]


if __name__ == '__main__':
    n = 10
    print(Solution().integerBreak(n))
