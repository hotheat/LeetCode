from collections import Counter


class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sc = Counter(s)
        tc = Counter(t)
        for i in tc:
            if i not in sc or sc[i] != tc[i]:
                return i


s = 'a'
t = 'aa'
print(Solution().findTheDifference(s, t))
