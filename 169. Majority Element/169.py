class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        cnt = {}
        for i, v in enumerate(nums):
            if v not in cnt:
                cnt[v] = 1
            else:
                cnt[v] += 1
                if cnt[v] > len(nums) / 2:
                    return nums[i]


arr = [2, 2, 1, 1, 1, 2, 2]
s = Solution()
print(s.majorityElement(arr))
