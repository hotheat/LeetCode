class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        caled = {}
        while n != 1:
            caled[n] = True

            res = 0
            for i in str(n):
                res += int(i) ** 2

            if res in caled:
                return False
            else:
                n = res
        return True


n = 123
print(Solution().isHappy(n))
