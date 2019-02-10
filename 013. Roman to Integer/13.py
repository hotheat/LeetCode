class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        ans = 0
        for i in range(len(s) - 1):
            if d[s[i]] >= d[s[i + 1]]:
                ans += d[s[i]]
            else:
                ans -= d[s[i]]
            print(ans)
        return ans + d[s[-1]]


def test(s):
    print(Solution().romanToInt(s))


# test("III")
test("IIV")
