这道题需要用栈来做，和基础班中词法解析类似，遇到左半部分压入栈，遇到右半部分弹出栈，判断弹出的元素是否和对应的左半部分相等。

注意处理 ''，'['，']' 的特殊情况。

类似的处理左右括号的都可以尝试用栈实现，还有[**032. Longest Valid Parentheses**](https://github.com/hotheat/LeetCode/tree/master/032.%20Longest%20Valid%20Parentheses)。