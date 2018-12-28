class Solution:
    def search(self, nums, target):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if nums[mid] < nums[high]:
                # 后半部分是排好序的
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                # 前半部分是排好序的
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3]
    target = 3
    print(s.search(nums, target) == 1)
    nums = [4, 5, 6, 7, 8, 1, 2]
    target = 1
    print(s.search(nums, target) == 5)
    nums = [3, 1]
    target = 1
    print(s.search(nums, target) == 1)
