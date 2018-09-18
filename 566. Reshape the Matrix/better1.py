class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # 这里 sum 的作用用来展开序列
        flat = sum(nums, [])
        if len(flat) != r * c:
            return nums
        tuples = zip(*([iter(flat)] * c))
        return list(map(list, tuples))


nums = [[1, 2, 3, 4],
        [3, 4, 5, 6]]
r = 4
c = 2
#
s = Solution()
print(s.matrixReshape(nums, r, c))
