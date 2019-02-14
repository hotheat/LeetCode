import operator


class Solution:
    def evalRPN(self, tokens: 'List[str]') -> 'int':
        stack = []
        ops = {'+': operator.add, '-': operator.sub, '*': operator.mul,
               '/': lambda x, y: int(operator.truediv(x, y))}

        for i in tokens:
            if not i in ops:
                stack.append(int(i))
            else:
                a, b = stack.pop(), stack.pop()
                stack.append(ops[i](b, a))
        return stack[0]


if __name__ == '__main__':
    tokens = ["4", "13", "5", "/", "+"]
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(Solution().evalRPN(tokens))
