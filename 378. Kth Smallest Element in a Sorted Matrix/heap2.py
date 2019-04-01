import heapq


class Solution():
    def kthSmallest(self, matrix, num):
        """
        返回 num 在 matrix 中的排名
        :param matrix:
        :param num:
        :return:
        """
        m, n = len(matrix), len(matrix[0])
        q = [(matrix[0][0], 0, 0)]

        for _ in range(num):
            ans, i, j = heapq.heappop(q)
            if j == 0 and i + 1 < m:
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n:
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
        return ans


if __name__ == '__main__':
    matrix = [[1, 2, 3, 7], [5, 10, 14, 16], [8, 10, 18, 19], [9, 12, 22, 24]]
    num = 14
    print(Solution().kthSmallest(matrix, num))
