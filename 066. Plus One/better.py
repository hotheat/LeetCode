class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == []:
            return [1]
        if digits[-1] == 9:
            digits = self.plusOne(digits[:-1]) + [0]
        else:
            digits[-1] += 1
        return digits


s = Solution()
arr = [9, 9, 9, 9]
print(s.plusOne(arr))
