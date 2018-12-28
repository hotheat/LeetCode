class Solution:
    def search(self, nums, target):
        if len(nums) <= 1:
            if len(nums) == 1:
                return 0 if nums[0] == target else -1
            return -1
        # 寻找旋转位置，返回转折点结束的位置
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                break
        if nums[i] == target:
            return i
        elif nums[0] <= target < nums[i]:
            return self.bsearch(nums[:i + 1], target)
        else:
            bres = self.bsearch(nums[i + 1:], target)
            return i + 1 + bres if bres != -1 else -1

    def bsearch(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 1
    s = Solution()
    print(s.search(nums, target))
