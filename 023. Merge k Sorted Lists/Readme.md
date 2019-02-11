`023.py` 利用 python 内置函数 `sorted` 对 array 进行排序。

`divide.py` 采用分治的思想，类似于[归并排序](https://github.com/hotheat/JiKeExcercise/blob/master/python-code/12_sorts/sortOnlogn.py)，先对 lists 进行划分，然后比较两个 List 的大小，最后合并。时间复杂度为 $O(nlogk)$， 两个 list 合并的时间复杂度为 $O(n)$，共有 $logk$ 次合并。

`sort_linked_list.py`，利用 sort 函数，最终以 linked list 呈现结果。

`primary_queue.py`，Python 中的 Primary Queue 用 heap 实现的，是在队列的基础上融合了堆的方法。传入的参数需要是一个元组，利用了元组比较的特性。可以参考[文章](https://zhuanlan.zhihu.com/p/37637660)。

代码参考[https://leetcode.com/problems/merge-k-sorted-lists/discuss/10607/Three-ways-to-solve-this-problem-inPython-(build-in-sort-merge-and-priority-queue)](https://leetcode.com/problems/merge-k-sorted-lists/discuss/10607/Three-ways-to-solve-this-problem-in-Python-(build-in-sort-merge-and-priority-queue))

讲解参考 [https://www.youtube.com/watch?v=5xT5GMTFvRI](https://www.youtube.com/watch?v=5xT5GMTFvRI)

