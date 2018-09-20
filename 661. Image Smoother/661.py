import math
from pprint import pprint


class Solution:

    def add_square(self, i, j, new_arr, M):
        """
        遍历 new_arr 元素，将对应的 M 中元素 M[i-1][j-1] 修改为平均值
        """
        loc = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
               (i, j - 1), (i, j), (i, j + 1),
               (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
        sum_i = 0
        cnt_i = 0
        for k in loc:
            if new_arr[k[0]][k[1]] != add_i:
                cnt_i += 1
                sum_i += new_arr[k[0]][k[1]]
        M[i - 1][j - 1] = math.floor(sum_i / cnt_i)

    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        new_arr = []
        global add_i
        add_i = float('inf')
        # 在 M 周围添加一圈行和列
        new_arr.append([add_i] * (len(M[0]) + 2))
        for i in M:
            new_arr.append([add_i] + i + [add_i])
        new_arr.append([add_i] * (len(M[0]) + 2))

        for i in range(1, len(new_arr) - 1):
            for j in range(1, len(new_arr[0]) - 1):
                self.add_square(i, j, new_arr, M)

        return M


M = [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]]
s = Solution()
print(s.imageSmoother(M))
