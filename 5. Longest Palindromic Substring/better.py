class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_right = 0
        center = 0
        s_add = '#'.join('^{}$'.format(s))
        searched = [0] * len(s_add)
        for i in range(1, len(s_add) - 1):
            if i < max_right:
                # 寻找 searched[j] 与 max_right-i 的最小值
                j = 2 * center - i
                searched[i] = min(searched[j], max_right - i)
            # 左右扩展判断
            while s_add[i - searched[i] - 1] == s_add[i + searched[i] + 1]:
                searched[i] += 1

            # 更新 center 及 max_right
            if i + searched[i] > max_right:
                center, max_right = i, i + searched[i]

        maxr, n = max((m, n) for n, m in enumerate(searched))

        return s[(n - maxr) // 2:(n + maxr) // 2]


if __name__ == '__main__':
    s = Solution()
    str = 'abae'
    # str = 'abbae'
    # str = 'abc'
    print(s.longestPalindrome(str))
