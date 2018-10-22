class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2 ** 31 or x < -2 ** 31: return 0
        x = list(str(x))
        flag = False
        if x[0] == '-':
            flag = True
            x = x[1:]

        i = 0
        while i < len(x) // 2:
            x[i], x[len(x) - (i + 1)] = x[len(x) - (i + 1)], x[i]
            i += 1

        if flag is True:
            x = int('-' + ''.join(x))
        else:
            x = int(''.join(x))

        if x > 2 ** 31 or x < -2 ** 31: return 0

        return x


x = -1230
print(Solution().reverse(x))
