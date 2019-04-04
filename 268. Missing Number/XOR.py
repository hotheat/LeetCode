class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
            print('miss', missing)
        return missing


if __name__ == '__main__':
    nums = [2, 0, 3]
    print(Solution().missingNumber(nums))
