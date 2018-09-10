from operator import add
from pprint import pprint


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        final = [[1]]
        for i in range(1, numRows):
            map_ = map(add, [0] + final[-1], final[-1] + [0])
            final.append(list(map_))
        return final if numRows else []


s = Solution()
pprint(s.generate(5))
