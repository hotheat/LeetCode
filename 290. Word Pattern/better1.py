class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p = pattern
        s = str.split()
        return list(map(p.find, p)) == list(map(s.index, s))
