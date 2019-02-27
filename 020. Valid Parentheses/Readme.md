这道题需要用栈来做，和基础班中词法解析类似，遇到左半部分压入栈，遇到右半部分弹出栈，判断弹出的元素是否和对应的左半部分相等。

注意处理 ''，'['，']' 的特殊情况。

类似的处理左右括号的都可以尝试用栈实现，还有[**032. Longest Valid Parentheses**](https://github.com/hotheat/LeetCode/tree/master/032.%20Longest%20Valid%20Parentheses)。

词法解析

```
parsed_ast
    tokens 是这样的 list (本例子有 9 个元素)
    ['[', '+', 12, '[', '-', 23, 45, ']', ']']

    从开始到结束, 把元素 push 入一个 栈 中
    碰到 ']' 元素就从 栈 中 pop 数据直到 pop 的是 '[' 元素
    把这些数据合并成一个 list 并逆序后再 push 入栈
    最终结果是一个只包含一个 list 元素的栈, list 元素如下
    ['+', 12, ['-', 23 45]]
    返回它
    :return: list
'''
```

```python
def parsed_ast(tokens):
    stack = []
    tmp = []
    for i in tokens:
        if i != ']':
            stack.append(i)
        else:
            while stack[-1] != '[':
                e = stack.pop()
                tmp.append(e)
            tmp_re = tmp[::-1]
            tmp = []
            stack.pop()
            stack.append(tmp_re)
    return stack[0]
```

