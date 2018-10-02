class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row, col = len(A), len(A[0])
        ans = []
        for c in range(col):
            ans.append([])
            for r in range(row):
                ans[c].append(A[r][c])
        return ans


A = [[1, 2, ], [4, 5, ], [7, 8, ]]
print(Solution().transpose(A))
