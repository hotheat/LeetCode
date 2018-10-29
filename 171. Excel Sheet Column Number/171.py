class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        number = dict(zip([chr(i) for i in range(65, 91)], range(1, 27), ))
        print(number)

        ans = 0
        length = len(s) - 1
        for i in s[:-1]:
            ans += 26 ** length * number[i]
            length -= 1
        return ans + number[s[-1]]


s = 'AAA'
print(Solution().titleToNumber(s))
