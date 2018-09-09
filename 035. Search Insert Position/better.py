class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        if nums[high] < target: return high + 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
            elif nums[mid] < target:
                if low == mid:
                    return low + 1
                low = mid
        return low


s = Solution()
arr = [1]
target = 0
print(s.searchInsert(arr, target))
