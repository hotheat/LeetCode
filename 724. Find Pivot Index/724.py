class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        s = sum(nums)
        tmp_sum = 0
        while i < len(nums):
            # 如果主元在第一个位置上，令主元左侧元素的加和为 0，否则，加和为主元左侧元素加和
            if i == 0:
                v = 0
            else:
                v = nums[i - 1]
            tmp_sum += v
            # 如果是主元，左侧元素加和等于右侧元素加和
            if tmp_sum != (s - nums[i]) / 2:
                i += 1
            else:
                return i
        return -1


# nums = [1, 2, -2, -1, -10]
# nums = [-1, -1, -1, 0, 1, 1]
nums = [1, 1, -1, 0, 1, 1]
s = Solution()
print(s.pivotIndex(nums))
