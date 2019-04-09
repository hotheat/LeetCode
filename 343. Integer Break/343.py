class Solution:
    max_res = float('-inf')

    def integerBreak(self, n: int) -> int:
        """
        回溯法
        假设 n=5，
        1*1*1*1*1
        ->1*1*1*2
        ->1*1*3
        ->1*4
        ->2*1*1*1
        ...
        :param n:
        :return:
        """

        self.helper(1, n + 1, 1, n)
        return Solution.max_res

    def helper(self, cur, remain, res, n):

        if remain == 1 and cur < n:
            Solution.max_res = max(Solution.max_res, res)
            return
        for i in range(cur, remain):
            self.helper(i, remain - i, res * i, n)


if __name__ == '__main__':
    print(Solution().integerBreak(3))
