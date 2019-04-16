from typing import List


class Solution:
    """
    维护一个递增数组，利用二分法寻找新元素的插入位置，插入到数组中
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = []

        for i in range(len(nums)):
            if len(res) == 0 or nums[i] > res[-1]:
                res.append(nums[i])
            else:
                insert_pos = self.divide_pos(res, nums[i])
                res[insert_pos] = min(res[insert_pos], nums[i])
        return len(res)

    def divide_pos(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        return start


if __name__ == '__main__':
    nums = [1, 4, 7, 5]
    print(Solution().lengthOfLIS(nums))
