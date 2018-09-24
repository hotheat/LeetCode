from collections import deque


# 提示深度优先搜索

class Solution:

    def is_range(self, arr, i, j):
        return 0 <= i < len(arr) and 0 <= j < len(arr[0])

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        searched = {}
        max_isl = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # 该点还没搜索过且这个点是岛屿，把它压入栈中
                if (r, c) not in searched and grid[r][c] == 1:
                    current_cnt = 0
                    stack = deque()
                    stack.append((r, c))
                    searched[(r, c)] = True
                    # 从栈顶弹出元素
                    while stack:
                        sr, sc = stack.pop()
                        current_cnt += 1
                        for nr, nc in ((sr - 1, sc), (sr, sc - 1), (sr, sc + 1), (sr + 1, sc)):
                            if self.is_range(grid, nr, nc) and grid[nr][nc] == 1 and (nr, nc) not in searched:
                                stack.append((nr, nc))
                                searched[(nr, nc)] = True
                    max_isl = max(max_isl, current_cnt)
        return max_isl


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

s = Solution()
print(s.maxAreaOfIsland(grid))
