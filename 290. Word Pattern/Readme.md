290.py 建立 pattern 映射到 s 和 s 映射到 pattern 的两个字典，分别做两次判断。解法比较笨重。

205，242，290 题都涉及了针对重复字符建立索引的问题。

better1.py 利用 find 和 index，使相同字母返回的索引相同，但这样时间复杂度会增加啊，每次都要查询一个字符的位置。

```python
In [3]: s = 'abab'

In [4]: list(map(s.find, s))
Out[4]: [0, 1, 0, 1]

In [8]: s = 'dog cat dog cat'.split()
    
In [10]: list(map(s.index, s))
Out[10]: [0, 1, 0, 1]
```

better2.py 定义一个辅助函数 `map_fault`，返回所有元素第一次出现时的索引列表，最后判断两个列表是否相等。

注意两点，

1. 返回元素第一次出现时的值，往往用到 `{}.setdefault(k, v)`，在 `697` 题中也用到过；

2. `setdefault` 接受两个参数，在使用 `map` 时，需要接受两个相同长度的列表作为参数，所以，`map_fault` 函数可以用一行表示。

```
In [11]: f = lambda s: map({}.setdefault, s, range(len(s)))

In [12]: f(pattern)
Out[12]: <map at 0xfa2ad68>

In [13]: list(f(pattern))
Out[13]: [0, 1, 0, 1]
```



better3.py 则利用 `set()` 去冗余的特点。