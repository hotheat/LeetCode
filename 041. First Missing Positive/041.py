class Solution:
    def firstMissingPositive(self, nums: 'List[int]') -> 'int':
        nums.sort()
        n = 1
        for i in nums:
            if i == n:
                n += 1
        return n


if __name__ == '__main__':
    nums = ([0, -1, 3, 1, 1], [4, 3, 4, 1, 1, 4, 1, 4], [1, 1, 2, 0])
    for n in nums:
        print(Solution().firstMissingPositive(n))
