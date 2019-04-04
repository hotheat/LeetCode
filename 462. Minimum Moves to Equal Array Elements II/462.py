class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        median = nums[len(nums) // 2]
        res = 0
        for i in nums:
            res += abs(i - median)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().minMoves2(nums))
