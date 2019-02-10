class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        num = ''
        for i, v in enumerate(str):
            # 保证第一个字符是 - 或 +，而且后面不再添加 + 或 -
            if not num and v in '+-':
                num = ''.join((num, v))
                continue
            # 符合数字
            if v.isdigit():
                num = ''.join((num, v))
            # 保证数字是连续出现
            elif ord(v) == 32 and not num:
                continue
            else:
                break

        # 不是空字符串或单独出现 + 或 -时
        if num and num != '+' and num != '-':
            if int(num) >= 0:
                return min(int(num), 2 ** 31 - 1)
            elif int(num) < 0:
                return max(int(num), -2 ** 31)
        else:
            return 0


if __name__ == '__main__':
    for s in ['+0 123', '+12 34', "4193 with words", "   -4  2", "words and 987", "-91283472332"]:
        sl = Solution()
        print(sl.myAtoi(s))
