from collections import Counter


class Solution:
    def findAnagrams(self, s, p):
        pc = Counter(p)
        sc = Counter(s[:len(p) - 1])
        res = []
        for i in range(len(p)-1, len(s)):
            # Counter 对于不存在的元素计数默认为 0，可以直接用累加
            sc[s[i]] += 1
            if sc == pc:
                res.append(i - (len(p) -1))
            # sc 最前面的元素计数减 1
            sc[s[i - (len(p) -1)]] -= 1
            if sc[s[i - (len(p) - 1)]] == 0:
                del sc[s[i - (len(p) - 1)]]
        return res


s = "cbaebabacd"
p = "abc"

print(Solution().findAnagrams(s, p))
