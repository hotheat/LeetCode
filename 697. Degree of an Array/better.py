from collections import Counter


class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, last = {}, {}
        for i, v in enumerate(nums):
            first.setdefault(v, i)
            last[v] = i
        c = Counter(nums)
        degree = max(c.values())
        return min(last[v] - first[v] + 1 for v in c if c[v] == degree)


nums = [1, 2, 2, 3, 1]
# nums = [1, 2, 2, 3, 1, 4, 2]
# nums = [1, 1]
s = Solution()
print(s.findShortestSubArray(nums))
