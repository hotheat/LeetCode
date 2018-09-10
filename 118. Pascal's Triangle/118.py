from pprint import pprint


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        final = [[1]]
        n = 1
        while n < numRows:
            level = []
            for i in range(1, n):
                level.append(final[n - 1][i-1] + final[n - 1][i])
            level = [1] + level + [1]
            final.append(level)
            n += 1
        return final if numRows else []


s = Solution()
pprint(s.generate(5))
