from itertools import accumulate
from typing import List


class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        first, last = 0, len(nums) - 1
        # 初始化 first，first 从第一个不是 0 的元素开始
        while first < len(nums) and nums[first] == 0:
            first += 1
        while last > 0 and nums[last] == 2:
            last -= 1

        index = first

        while index <= last:
            if nums[index] == 1:
                index += 1
            elif nums[index] == 0:
                nums[first], nums[index] = nums[index], nums[first]
                first += 1
                index += 1
            elif nums[index] == 2:
                nums[index], nums[last] = nums[last], nums[index]
                last -= 1


if __name__ == '__main__':
    nums = [0]
    Solution().sortColors(nums)
    print(nums)
