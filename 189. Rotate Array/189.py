class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            pass
        else:
            nums[:k], nums[k:] = nums[-k:], nums[:-k],


s = Solution()
nums = [1, 2, 3, ]
k = 5
for i in range(k):
    print(i)
    s.rotate(nums, i)
    print(nums)
