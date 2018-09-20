在原始列表的基础上添加一圈或者通过
```python
def inRange(self, arr, i, j):
    return i >= 0 and i < len(arr) and j >= 0 and j < len(arr[0])
```
的方法判断是否是在顶点或者边上。

时间复杂度 $O(n)$，空间复杂度 $O(n)$
