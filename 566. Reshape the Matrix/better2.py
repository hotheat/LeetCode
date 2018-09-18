class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums
        else:
            items = [y for x in nums for y in x]
            return [items[x * c: ((x + 1) * c)] for x in range(r)]


nums = [[1, 2, 3, 4],
        [3, 4, 5, 6]]
r = 4
c = 2

s = Solution()
print(s.matrixReshape(nums, r, c))
