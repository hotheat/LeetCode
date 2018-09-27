class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        d = {0: 1, 1: 0}
        for row in A:
            i, j = 0, len(row) - 1
            # 行中元素个数为奇数
            while i < len(row) // 2:
                row[i], row[j] = d[row[j]], d[row[i]]
                i += 1
                j -= 1
            # 判断行中元素个数为奇数的情况
            if len(row) % 2 == 1:
                row[len(row) // 2] = 1 - row[len(row) // 2]
        return A


A = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
print(Solution().flipAndInvertImage(A))
