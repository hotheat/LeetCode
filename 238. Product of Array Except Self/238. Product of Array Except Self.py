from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        if len(nums) <= 1:
            return nums

        res[0] = 1
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        mul = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * mul
            mul = mul * nums[i]
        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(Solution().productExceptSelf(nums))
