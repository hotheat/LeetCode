import sys


class Solution:
    def firstMissingPositive(self, nums):
        maxint = sys.maxsize
        if not nums:
            return 1
        for i, v in enumerate(nums):
            if v <= 0:
                nums[i] = maxint

        for i, v in enumerate(nums):
            ix = abs(v) - 1
            if ix < len(nums):
                nums[ix] = -abs(nums[ix])

        for i, v in enumerate(nums):
            if v > 0:
                return i + 1
        return len(nums) + 1


if __name__ == '__main__':
    nums = ([0, -1, 3, 1, 1], [4, 3, 6, 5, 3, 4, 1], [1, 1, 2, 0])
    # nums = ([2], [3, 4, -1, 1])
    for n in nums:
        print(Solution().firstMissingPositive(n))
