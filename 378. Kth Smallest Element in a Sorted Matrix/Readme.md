题眼是 `sorted matrix`，所以 `378.py` 中用堆的方法解决会慢很多。

matrix 的排序方式是按行来看是排序好的，按列也是排序好的，但总体来看，不一定是有序的。

`bisection.py` 从左上角到右下角的阶梯型遍历

`heap2.py`，在 j=0 时向下扩展，否则只向右扩展，堆的优化

[<http://bookshadow.com/weblog/2016/08/01/leetcode-kth-smallest-element-in-a-sorted-matrix/>](http://bookshadow.com/weblog/2016/08/01/leetcode-kth-smallest-element-in-a-sorted-matrix/)