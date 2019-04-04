class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x = 0
        for n in nums:
            x ^= n
        ## 制造分离因子，将两组数分开，不妨就找出这两个数二进制表示中从右到左第一个不相同的数
        mask = 1
        while mask & x == 0:
            mask = mask << 1
        # mask 的形式 000010000，只会有一个 1，这个位置就是 a 与 b 不同的位置
        # 利用分离因子，将与 a 相同的分成一组，与 b 相同的分成一组
        a, b = 0, 0
        for i in nums:
            if i & mask == 0:
                a ^= i
            else:
                b ^= i
        return [a, b]


if __name__ == '__main__':
    nums = [1, 2, 1, 2, 3, 5]
    print(Solution().singleNumber(nums))
