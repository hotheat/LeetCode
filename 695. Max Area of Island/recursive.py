class Solution:

    def is_range(self, arr, i, j):
        return 0 <= i < len(arr) and 0 <= j < len(arr[0])

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        searched = set()

        def area(r, c):
            if not (self.is_range(grid, r, c) and grid[r][c] == 1 and (r, c) not in searched):
                return 0
            searched.add((r, c))
            return 1 + area(r + 1, c) + area(r - 1, c) + \
                   area(r, c - 1) + area(r, c + 1)

        return max(area(r, c) for r in range(len(grid)) for c in range(len(grid[0])))


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
