from collections import Counter


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = Counter(s)
        for i, v in enumerate(s):
            if cnt[v] == 1:
                return i
        return -1


s = "leetcode"
s = "loveleetcode"
print(Solution().firstUniqChar(s))
