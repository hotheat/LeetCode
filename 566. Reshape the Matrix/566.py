class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        res = []
        i, j = 0, 0
        # 从原始列表 nums 中的索引
        current_r, current_c = 0, 0
        while current_r < r:
            # 新增一行，列标初始化为 0
            current_c = 0
            res.append([])
            while current_c < c:
                # 从原列表取数，超过列数后，行标加 1，列标归 0
                if j >= len(nums[0]):
                    j = 0
                    i += 1
                # 取数超过列数，返回原始列表
                if i >= len(nums):
                    return nums
                res[current_r].append(nums[i][j])
                # 原始列表列数加 1
                j += 1
                current_c += 1
            current_r += 1
        return res


nums = [[1, 2, 3, 4],
        [3, 4, 5, 6]]
r = 3
c = 4

s = Solution()
print(s.matrixReshape(nums, r, c))
