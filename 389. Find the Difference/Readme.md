str.find(str, [s=0], [e=str.length]) 函数，从 s 处向右查找 str，结束处索引为 e，s 默认为 0，e 默认为字符串长度

```python
In [1]: s = 'abcd'

In [3]: s.find('a', -1)
Out[3]: -1

In [4]: s.find('a',)
Out[4]: 0

In [5]: s.find('a', -2)
Out[5]: -1
    
In [9]: s.find('d', -1)
Out[9]: 3

In [10]: s.find('a', -4)
Out[10]: 0
```

xor.py 

异或公式记住 
$$
a \oplus a = 0 \\
0 \oplus b = b \\
a\oplus b \oplus a = a \oplus a \oplus b = b
$$
other.py

Counter() 的集合运算（交集、并集和叉集）

```python
In [34]: s = 'aaabbc'

In [35]: t = 'aaabbbc'

In [36]: sc = Counter(s)

In [37]: tc = Counter(t)

In [38]: dict(sc & tc)
Out[38]: {'a': 3, 'b': 2, 'c': 1}

In [39]: dict(tc | sc)
Out[39]: {'a': 3, 'b': 3, 'c': 1}

In [40]: dict(tc - sc)
Out[40]: {'b': 1}
```