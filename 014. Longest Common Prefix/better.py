class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s = ''
        for i in zip(*strs):
            if len(set(i)) != 1:
                return s
            else:
                s += i[0]

        return s


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    strs = ["dog", "racecar", "car"]
    # strs = ["caa", "a", "acb"]
    print(Solution().longestCommonPrefix(strs))