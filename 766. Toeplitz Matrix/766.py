class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        pre = matrix[0]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] != pre[j - 1]:
                    return False
            pre = matrix[i]
        return True


matrix = [
    [1, 2, 3, 4],
    [5, 1, 2, 3],
    [9, 5, 1, 2]
]
matrix = [
    [1, 2],
    [2, 2]
]
print(Solution().isToeplitzMatrix(matrix))
