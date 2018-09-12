class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(numbers) - 1
        while start < end:
            tmp = numbers[start] + numbers[end]
            if tmp == target:
                return start + 1, end + 1
            elif tmp < target:
                start += 1
            else:
                end -= 1


arr = [2, 7, 11, 15]
s = Solution()
print(s.twoSum(arr, 9))
