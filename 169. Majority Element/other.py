class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums) // 2]


arr = [2, 2, 1, 1, 1, 2, 2]
s = Solution()
print(s.majorityElement(arr))
