class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt = 0
        searched = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k and (
                        (nums[i], nums[j]) not in searched and
                        (nums[j], nums[i]) not in searched):
                    searched[(nums[i], nums[j])] = 1
                    cnt += 1
        return cnt


nums = [3, 1, 4, 1, 5]
k = 2
nums = [1, 2, 3, 4, 5]
k = 1
nums = [1, 3, 1, 5, 4]
k = 0
s = Solution()
print(s.findPairs(nums, k))
