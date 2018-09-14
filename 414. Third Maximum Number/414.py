class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fir, sec, thr = float('-inf'), float('-inf'), float('-inf')
        for i in nums:
            if i > fir:
                thr = sec
                sec = fir
                fir = i
            elif sec < i < fir:
                thr = sec
                sec = i
            elif thr < i < sec:
                thr = i
        for i in [fir, sec, thr]:
            if i == float('-inf'):
                return fir
        return thr


nums = [1, 2]
s = Solution()
print(s.thirdMax(nums))
