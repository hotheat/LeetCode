- 566.py

  思路：

  并没有先 flatten；

  只要行数 $< r$，就新增一行，且列标归 0；

  只要从原始列表取数的列索引超过列数，那么去下一行取；

  只要从原始列表取数的行索引超过行数，那么返回原列表。

- better1.py

  1. 列表 flatten 的方法

  ``` python
  #flatten the lis
  for x in list_of_lists:
      for y in x:
          flattened_list.append(y)
  ```

  ``` python
  #flatten the lists
  flattened_list = [y for x in list_of_lists for y in x]
  ```

  itertools 的使用参考 [http://www.wklken.me/posts/2013/08/20/python-extra-itertools.html#itertoolsisliceiterable-stop](http://www.wklken.me/posts/2013/08/20/python-extra-itertools.html#itertoolsisliceiterable-stop)

  `itertools.chain()` 将多个迭代器作为参数，返回单个迭代器，产生所有参数迭代器的内容

  ``` python
  import itertools
  flattened_list  = list(itertools.chain(*list_of_lists))
  ```

  ``` python
  flattenedlist = sum(listof_lists, [])
  ```

  2. zip()

  zip(*list) 类似于反解压

  ```python
  In [6]: l = [(1, 4), (2, 5), (3, 6)]
  
  In [7]: list(zip(*l))
  Out[7]: [(1, 2, 3), (4, 5, 6)]
  ```

- better2.py

  采用先 flatten，而后索引的方法。

  索引还可以采用 `itertools.islice()`，创建一个迭代器，采用切片的方式，每个迭代在 stop 处停止。

  ``` python
  def matrixReshape(self, nums, r, c):
      if r * c != len(nums) * len(nums[0]):
          return nums
      it = itertools.chain(*nums)
      return [list(itertools.islice(it, c)) for _ in xrange(r)]
  ```
