from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = [1] * (len(nums) + 1)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    res[i] = max(res[i], res[j] + 1)
        return max(res)


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(Solution().lengthOfLIS(nums))
