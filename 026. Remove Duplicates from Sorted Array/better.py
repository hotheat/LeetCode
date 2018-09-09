class Solution(object):
    def removeDuplicates(self, nums):
        """
        仅仅输出计数, 没有对数组进行修改
        """
        if len(nums) == 0:
            return 0
        # 定义两个指针，快指针 i，慢指针 j
        i, j = 0, 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                # 不考虑超出新长度后面的元素
                nums[j] = nums[i]
            # 如果出现重复值时，快指针 i 将比慢指针 j 走得快
            else:
                continue
        return j + 1


nums = [1, 1, 2, 3, 4, 4, 5, 5, 6]
s = Solution()
print(s.removeDuplicates(nums))
