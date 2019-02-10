class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        pre = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(pre) != 0:
                pre = pre[:-1]
            if not pre:
                break
        return pre


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    strs = ["dog", "racecar", "car"]
    # strs = ["caa", "a", "acb"]
    print(Solution().longestCommonPrefix(strs))