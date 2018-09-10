from operator import add


class Solution:
    def get_row_iter(self, rowIndex, res):
        if rowIndex not in res:
            res[rowIndex] = list(
                map(add,
                    [0] + self.get_row_iter(rowIndex - 1, res),
                    (self.get_row_iter(rowIndex - 1, res) + [0])
                    )
            )
        return res[rowIndex]

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = {0: [1]}
        return self.get_row_iter(rowIndex, res)


s = Solution()
print(s.getRow(100))
