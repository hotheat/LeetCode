350.py 同样利用双指针法，相等时指针同时加 1，否则较小数的指针加 1.

better1.py

1. collections.Counter() 返回类似字典的结构，value 是元素的出现次数。532 题中也有用到
2. collections.Counter() 的返回值可以直接做交集运算，这是字典不具备的。elements() 方法返回 [key] 乘以 value 的列表

```python
In [5]: c1 = [1, 2, 2, 3]

In [6]: c2 = [1, 1, 2, 2]
   
In [20]: Counter(c1)
Out[20]: Counter({1: 1, 2: 2, 3: 1})

In [21]: d = dict(Counter(c1))

In [22]: d
Out[22]: {1: 1, 2: 2, 3: 1}

In [23]: d2 = dict(Counter(c1))

In [24]: d & d2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-24-fc5a2e57bbd3> in <module>()
----> 1 d & d2

TypeError: unsupported operand type(s) for &: 'dict' and 'dict'

In [25]: Counter(c1) & Counter(c2)
Out[25]: Counter({1: 1, 2: 2})
```

3. sum(iterable[, start]) 

   ![](https://upload-images.jianshu.io/upload_images/1095290-7e9dbd3b331d21f2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)

   ```python
   In [10]: sum([[1], [2, 2]], [])
   Out[10]: [1, 2, 2]
   ```

   传入空列表作为初值，对可迭代对象进行连接。可以作为一种列表展平的方法，而列表展平官方推荐的方法是使用 `itertools.chain()`

   ```python
   In [13]: from itertools import chain
       
   In [17]: list(chain(*[[1], [2, 2]]))
   Out[17]: [1, 2, 2]
   
   In [18]: list(chain(*[[1], [2, 2], [3]]))
   Out[18]: [1, 2, 2, 3]
   
   In [19]: list(chain(*[[1], [2, [1, 2]], [3]]))
   Out[19]: [1, 2, [1, 2], 3]
   ```

   其他列表展平的方法参考 [https://www.chenyudong.com/archives/python-make-flat-list-of-list.html](https://www.chenyudong.com/archives/python-make-flat-list-of-list.html)

