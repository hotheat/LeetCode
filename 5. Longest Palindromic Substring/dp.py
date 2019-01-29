class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, max_length = 0, 0
        length = len(s)
        dp = [[None] * length for _ in range(length)]

        # 一个字符串时肯定是回文
        for i in range(length):
            dp[i][i] = True
            max_length = 1

        # 两个字符串，判断两个字符串是否相等
        for i in range(length - 1):
            j = i + 1
            if s[i] == s[j]:
                dp[i][j] = True
                max_length = 2
                start = i
            else:
                dp[i][j] = False

        # 超过 3 个字符串，按每一列来填表
        for col in range(2, length):
            for row in range(col - 1):
                # 是回文字符串
                if s[row] == s[col] and dp[row + 1][col - 1] is True:
                    dp[row][col] = True
                    if col - row + 1 > max_length:
                        max_length = col - row + 1
                        start = row
                else:
                    dp[row][col] = False

        return s[start:start + max_length]


if __name__ == '__main__':
    for s in  ['b', 'ba', 'bb', 'befeg', 'abccbe']:
        sl = Solution()
        print(sl.longestPalindrome(s))
