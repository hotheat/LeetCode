class Solution:
    def isValid(self, s: 'str') -> 'bool':
        d = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if not i in d:
                stack.append(i)
            else:
                # ']' 这种情况
                if not stack:
                    return False
                elif stack.pop() == d[i]:
                    continue
                else:
                    return False

        return True if not stack else False


if __name__ == '__main__':
    s = "]"
    print(Solution().isValid(s))
