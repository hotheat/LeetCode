class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if len(s) < 2:
            return s

        max_length = 0

        for i in range(len(s)):
            # 奇数情况
            j = 0
            while i - j >= 0 and i + j < length:
                if s[i - j] == s[i + j]:
                    l = j * 2 + 1
                    if l > max_length:
                        max_length = l
                        max_str = s[i - j:i + j + 1]
                else:
                    break
                j += 1

            # 偶数情况
            j = 0
            while i - j >= 0 and i + j + 1 < length:
                if s[i - j] == s[i + j + 1]:
                    l = j * 2 + 2
                    if l > max_length:
                        max_length = l
                        max_str = s[i - j: i + j + 1 + 1]
                else:
                    break
                j += 1

        return max_str


if __name__ == '__main__':
    s = Solution()
    str = 'abae'
    str = 'abbae'
    str = 'abc'
    print(s.longestPalindrome(str))
