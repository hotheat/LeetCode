class Solution:

    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])

        def is_square(a, b, c, d, e, f, g, h, i):
            return (sorted([a, b, c, d, e, f, g, h, i]) == list(range(1, 10)) and
                    (a + b + c == d + e + f == g + h + i == a + d + g ==
                     b + e + h == c + f + i == a + e + i == c + e + g == 15))

        ans = 0
        for r in range(R - 2):
            for c in range(C - 2):
                if grid[r + 1][c + 1] != 5: continue  # optional skip
                if is_square(grid[r][c], grid[r][c + 1], grid[r][c + 2],
                             grid[r + 1][c], grid[r + 1][c + 1], grid[r + 1][c + 2],
                             grid[r + 2][c], grid[r + 2][c + 1], grid[r + 2][c + 2]):
                    ans += 1
        return ans


grid = [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]
print(Solution().numMagicSquaresInside(grid))

