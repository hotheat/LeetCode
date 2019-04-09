from typing import List
from itertools import accumulate


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        # 初始化
        dp[0] = list(accumulate(grid[0]))
        first_col = list(accumulate(i[0] for i in grid))
        for i in range(len(dp)):
            dp[i][0] = first_col[i]

        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])

        return dp[-1][-1]


if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(Solution().minPathSum(grid))
