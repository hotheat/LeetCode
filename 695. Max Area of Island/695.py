from collections import deque

# 提示深度优先搜索

class Solution:

    searched = {}

    def is_range(self, arr, i, j):
        return 0 <= i < len(arr) and 0 <= j < len(arr[0])

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    Solution.searched[(i, j)] = True
                    if (i, j) not in