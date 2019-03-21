from itertools import accumulate
from typing import List


class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums

        count_lst = [0] * (max(nums) + 1)
        for i in nums:
            count_lst[i] += 1

        count_lst = list(accumulate(count_lst))
        sorted_lst = [0] * len(nums)

        for i in nums:
            idx = count_lst[i] - 1
            sorted_lst[idx] = i
            count_lst[i] -= 1

        for i, v in enumerate(sorted_lst):
            nums[i] = v


if __name__ == '__main__':
    nums = [2, 1, 0, 1, 2, 0]
    print(Solution().sortColors(nums))
