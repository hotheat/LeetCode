class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 记录修改次数
        cnt = 0
        # 循环指针
        i = 0
        while i < len(nums) - 1 and cnt <= 1:
            if nums[i] > nums[i + 1]:
                cnt += 1
                if i == 0:
                    nums[i] = nums[i + 1]
                elif nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                elif nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]
            i += 1
        return cnt <= 1


nums = [4, 2, 3]
s = Solution()
print(s.checkPossibility(nums))
