class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1s = 0
        cnt1s = 0
        for i in nums:
            if i == 1:
                cnt1s += 1
            elif i == 0:
                if cnt1s > max1s:
                    max1s = cnt1s
                cnt1s = 0
        return max(max1s, cnt1s)


nums = [1, 1, 0, 1, 1,]
s = Solution()
print(s.findMaxConsecutiveOnes(nums))
