遇到括号匹配，算术运算这种，考虑用栈来做。

注意几点，

1. python 中的地板除 //，1//-2 = -1，而 leetcode 中要求这样的除法返回 0，需要重新包装一下除法。
2. 将运算后的结果也压入栈中，同时弹出两个值
3. 在除法和减法中，注意弹出元素运算的先后顺序

这道题属于词法解析的范围，萧大基础班中有这样一道题

```
tokens 是这样的 list (本例子有 9 个元素)
['[', '+', 12, '[', '-', 23, 45, ']', ']']

从开始到结束, 把元素 push 入一个 栈 中
碰到 ']' 元素就从 栈 中 pop 数据直到 pop 的是 '[' 元素
把这些数据合并成一个 list 并逆序后再 push 入栈
最终结果是一个只包含一个 list 元素的栈, list 元素如下
['+', 12, ['-', 23 45]]
返回它
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

