class Solution():
    def reverseWords(self, s: str) -> str:
        start = 0
        res = ''
        if not s:
            return ''
        for i in range(len(s)):
            if s[i] == ' ':
                res += s[start:i][::-1]
                res += ' '
                start = i + 1
            else:
                continue
        if start + 1 <= len(s):
            res += s[start:][::-1]
        return res


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    s = "hehhhhhhe"

    # s = ' abc def '
    # s = ' '
    print(Solution().reverseWords(s), len(s), len(Solution().reverseWords(s)))
