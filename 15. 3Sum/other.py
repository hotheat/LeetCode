class Solution:
    def threeSum(self, nums):

        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                # 如果 i 与上一个值相同，那么就跳过该值
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    # 只是在正确结果中判断是否重复，move left
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    # move right
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
