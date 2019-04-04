class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = set()
        for i in nums:
            if i not in tmp:
                tmp.add(i)
            else:
                tmp.remove(i)
        return list(tmp)


if __name__ == '__main__':
    nums = [1, 2, 1, 2, 3, 5]
    print(Solution().singleNumber(nums))
