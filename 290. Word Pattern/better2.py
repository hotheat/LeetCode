class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        def map_fault(s):
            d = {}
            res = []
            for i, v in zip(s, range(len(s))):
                res.append(d.setdefault(i, v))
            return res

        return map_fault(pattern) == map_fault(str.split())


pattern = "abba"
str = "dog cat cat dog"
print(Solution().wordPattern(pattern, str))
