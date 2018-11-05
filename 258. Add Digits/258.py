class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            temp = 0
            while num > 0:
                temp += num % 10
                num //= 10
            num = temp
        return num

num = 1
print(Solution().addDigits(num))