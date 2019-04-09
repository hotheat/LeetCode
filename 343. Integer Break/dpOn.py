class Solution:

    def integerBreak(self, n: int) -> int:
        """
        经过观察可以发现，除 n=1,2,3外，最大乘积均有 2 或 3 组成
        :param n:
        :return:
        """
        if n < 4:
            return n - 1
        res = [1] * (n + 1)
        res[2], res[3] = 2, 3

        for i in range(4, n + 1):
            res[i] = max(2 * res[i - 2], 3 * res[i - 3])
        return res[n]


if __name__ == '__main__':
    n = 10
    print(Solution().integerBreak(n))
