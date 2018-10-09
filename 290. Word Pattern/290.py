class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) != len(str.split()):
            return False
        d1, d2 = {}, {}
        for (i, v) in zip(pattern, str.split()):
            tmp1, tmp2 = d1.get(i), d2.get(v)
            if tmp1 is None and tmp2 is None:
                d1[i] = v
                d2[v] = i
            elif tmp1 != v or tmp2 != i:
                return False
        return True


pattern = "abba"
str = "dog cat dog dog"
print(Solution().wordPattern(pattern, str))
