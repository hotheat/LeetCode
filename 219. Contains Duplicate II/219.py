class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        tmp = {}
        for i, v in enumerate(nums):
            if v in tmp and i - tmp[v] <= k:
                return True
            tmp[v] = i
            print(tmp)
        return False


s = Solution()
nums = [1, 2, 3, 1]
k = 3
print(s.containsNearbyDuplicate(nums, k))
