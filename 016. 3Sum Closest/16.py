class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = sum(nums[:3])
        length = len(nums)
        i = 0
        while i < length - 2:

            pre, beh = i + 1, length - 1
            while pre < beh:
                s = nums[i] + nums[pre] + nums[beh]
                if s == target:
                    return s
                elif s < target:
                    pre += 1
                else:
                    beh -= 1

                if abs(s - target) < abs(result - target):
                    result = s
            i += 1
        return result


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    print(Solution().threeSumClosest(nums, 1))
