import collections


class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        cnt = collections.Counter(nums)
        for c in cnt:
            if k > 0 and c + k in cnt or k == 0 and cnt[c] > 1:
                res += 1
        return res
