class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        for i in range(0, len(strs) - 1):
            res = ''
            fir = 0

            while fir < len(strs[i]) and fir < len(strs[i + 1]):
                if strs[i][fir] == strs[i + 1][fir]:
                    res = ''.join((res, strs[i][fir]))
                else:
                    break
                fir += 1
            if not res:
                break
            # 将下一组要判断的第一个字符串记为 res
            strs[i+1] = res
        return res


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    strs = ["dog", "racecar", "car"]
    # strs = ["caa", "a", "acb"]
    print(Solution().longestCommonPrefix(strs))
