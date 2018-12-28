class Solution:
    def search(self, nums, target):
        if len(nums) <= 1:
            if len(nums) == 1:
                return 0 if nums[0] == target else -1
            return -1
        # 利用二分法寻找转折点，返回原数组开始位置
        start, end = 0, len(nums) - 1
        while start <= end:
            if end - start == 1:
                if nums[start] < nums[end]:
                    twist = start
                else:
                    twist = end
                break
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid
        i = twist
        if nums[i] == target:
            return i
        # 注意边界为 0 的情况
        elif i != 0 and nums[0] <= target <= nums[i - 1]:
            return self.bsearch(nums[:i], target)
        else:
            bres = self.bsearch(nums[i:], target)
            return i + bres if bres != -1 else -1

    def bsearch(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        print('nums', nums)
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
    s = Solution()
    nums = [1, 3]
    target = 3
    print(s.search(nums, target))
    nums = [4, 5, 6, 7, 8, 1, 2]
    nums = [3, 1]
    # nums = [2, 3, 4, 5, 6, 7, 1]
    target = 1
    print(s.search(nums, target))
    # target = 5
    # print(s.search(nums, target))
    # target = 4
    # print(s.search(nums, target))
    # target = 10
    # print(s.search(nums, target))
