from collections import Counter


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        sc = Counter(p)
        res = []
        for i in range(len(s)):
            tmp = s[i: i + len(p)]
            if sc == Counter(tmp):
                res.append(i)
        return res


s = "cbaebabacd"
p = "abc"
print(Solution().findAnagrams(s, p))