class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        searched = {}
        for i, v in enumerate(numbers):
            other = target - v
            if other in searched:
                return searched[other] + 1, i + 1
            else:
                searched[v] = i


arr = [2, 7, 11, 15]
s = Solution()
print(s.twoSum(arr, 9))
