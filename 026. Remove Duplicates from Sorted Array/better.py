class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        slow = 1
        for h in range(1, len(nums)):
            if nums[h] != nums[h - 1]:
                nums[slow] = nums[h]
                slow += 1
        return slow


nums = [1, 1, 2, 3, 4, 4, 5, 5, 6]
s = Solution()
print(s.removeDuplicates(nums))
