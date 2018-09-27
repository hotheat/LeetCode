class Solution:
    def flipAndInvertImage(self, A):
        return [[1 - i for i in row[::-1]] for row in A]


A = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
# A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
print(Solution().flipAndInvertImage(A))
