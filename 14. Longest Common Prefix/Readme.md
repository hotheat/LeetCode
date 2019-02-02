`14.py` 思路：先判断前两个字符串公共的部分，将公共部分与下一个字符串再进行判断，如果公共部分有 '' 出现，则停止判断。

`better.py` 利用 zip 与 set 进行判断。

`*` 与 `**` 分别可以用于迭代器及字典的解包

```
In [4]: s = ['ab', 'cd', 'de']

In [5]: print(*s)
ab cd de

In [21]: def myfun(a, b, c):
    ...:     print(a, b, c)

In [22]: s = {'a': 1, 'b':2, 'c':3}

In [23]: myfun(**s)
1 2 3
```

`better2.py` 参考 [https://leetcode.com/problems/longest-common-prefix/discuss/6910/Java-code-with-13-lines](https://leetcode.com/problems/longest-common-prefix/discuss/6910/Java-code-with-13-lines)
利用 str.find 方法，寻找 pre 在目标字符串中的 index，如果 index 不等于 0，每次缩短 pre 一位。同时 string.find(s)，当 s 为空时，返回 0，找不到时返回 -1。

还可以先找出列表中最短的字符串，再比较公共前缀。