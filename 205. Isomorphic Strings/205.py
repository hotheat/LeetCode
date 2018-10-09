class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def check(s, t):
            word_map = {}
            for i, v in enumerate(s):
                tmp = word_map.get(t[i])
                if tmp is None:
                    word_map[t[i]] = s[i]
                    tmp = s[i]
                t = t[:i] + tmp + t[i + 1:]
            return s == t
        return check(s, t) and check(t, s)


s = 'title'
t = 'paper'
# t = 'title'
# s = 'paler'
print(Solution().isIsomorphic(s, t))
