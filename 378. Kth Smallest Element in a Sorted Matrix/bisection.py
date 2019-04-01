class Solution():
    def count_lower(self, matrix, num):
        """
        返回 num 在 matrix 中的排名
        :param matrix:
        :param num:
        :return:
        """
        i, j = len(matrix) - 1, 0
        cnt = 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] <= num:
                cnt += i + 1
                j += 1
            else:
                i -= 1
        return cnt

    def kthSmallest(self, matrix, k):
        low, high = matrix[0][0], matrix[-1][-1]
        # 这里需要等号成立
        while low <= high:
            mid = (high - low) / 2 + low
            loc = self.count_lower(matrix, mid)
            if loc >= k:
                high = mid - 1
            else:
                low = mid + 1
        return low


if __name__ == '__main__':
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    print(Solution().kthSmallest(matrix, 8))
