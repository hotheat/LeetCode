class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.nums = nums
        self.length = len(self.nums)
        res = []

        i = 0
        while i < self.length - 2:
            pre = i + 1
            beh = self.length - 1
            while pre < beh:
                s = self.nums[i] + self.nums[pre] + self.nums[beh]
                if s == 0:
                    res.append([self.nums[i], self.nums[pre], self.nums[beh]])
                    beh = self.move_left(beh - 1)
                    pre = self.move_right(pre + 1)
                elif s < 0:
                    pre = self.move_right(pre + 1)
                else:
                    beh = self.move_left(beh - 1)
            i = self.move_right(i + 1)

        return res

    def move_left(self, ix):
        while ix == self.length - 1 or (ix >= 0 and self.nums[ix] == self.nums[ix + 1]):
            ix -= 1
        return ix

    def move_right(self, ix):
        while ix == 0 or (ix < self.length and self.nums[ix] == self.nums[ix - 1]):
            ix += 1
        return ix


if __name__ == '__main__':
    nums = [-4, -1, -1, 0, 1, 2]
    print(Solution().threeSum(nums))
    nums = [-1, 0, 1, 1, 2, 3]
    print(Solution().threeSum(nums))
