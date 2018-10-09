class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n1, n2 = [0] * 256, [0] * 256
        for i in s:
            n1[ord(i)] += 1
        for i in t:
            n2[ord(i)] += 1
        return n1 == n2


s = 'top'
t = 'cat'
print(Solution().isAnagram(s, t))
