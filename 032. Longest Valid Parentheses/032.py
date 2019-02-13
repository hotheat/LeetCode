class Solution:
    def longestValidParentheses(self, s: 'str') -> 'int':
        maxlen, leftmost = 0, -1
        stack = []
        for i, v in enumerate(s):
            if v=='(':
                stack.append(i)
            else:
                if not stack:
                    leftmost = i
                else:
                    p = stack.pop()
                    if stack:
                        maxlen = max(maxlen, i - stack[-1])
                    else:
                        maxlen = max(maxlen, i-leftmost)
        return maxlen


if __name__ == '__main__':
    s = "(()))(()"
    s = "(()()"
    print(Solution().longestValidParentheses(s))
