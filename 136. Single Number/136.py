class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        searched = {}
        for i in nums:
            if i in searched:
                del searched[i]
            else:
                searched[i] = True
        return list(searched.keys())[0]


nums = [4, 1, 2, 1, 2]
print(Solution().singleNumber(nums))
