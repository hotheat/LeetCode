class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        intg = int(''.join([str(i) for i in digits]))
        intg += 1
        res = [int(i) for i in str(intg)]
        return res


s = Solution()
digits = [9, 19, 9, 9]
print(s.plusOne(digits))
