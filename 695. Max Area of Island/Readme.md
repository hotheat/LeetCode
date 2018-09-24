这道题用 DFS 的思路求解，一个是循环结构的写法，一个是递归的写法
从可读性来看，递归更容易理解；
从运行效率来看，循环的效率要高一些。

```python
%timeit s.maxAreaOfIsland_rec(grid)

173 µs ± 8.12 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%timeit s.maxAreaOfIsland(grid)

111 µs ± 8.63 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
```