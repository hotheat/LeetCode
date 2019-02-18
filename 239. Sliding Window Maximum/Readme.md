该题解可以有三种方法

1. 暴力解决法

   `239.py`，时间复杂度为 $O((n-k+1)\times k)$，滑动窗口，每次找出最大值，加入列表。空间复杂度可以做到  $O(1)$，

2. priority queue

   每次加入的元素放到 priority queue 中，取元素时，先从堆中将前一个元素删除，再取堆顶元素即可，插入元素的时间复杂度是 $O(logk)$，删除元素的时间复杂度是 $O(logk)$，整个题目的时间复杂度是 $O(n\times 2\times logk)$。

3. Monotonic queue

   实际上，这道题目的本意是实现时间复杂度为 $O(n)​$，用单调递减的序列 deque 来做。

   **queue 中并不存储窗口的值，而是窗口元素的下标**。

   单调递减序列 deque 长度不超过 k，deque 的头元素便是最大值。

   [https://www.youtube.com/watch?v=G70qltIBF40](https://www.youtube.com/watch?v=G70qltIBF40)

   ![mark](http://qnpic.sijihaiyang.top/blog/20190218/nmNYhFIGUgPz.png?imageslim)

   ![mark](http://qnpic.sijihaiyang.top/blog/20190218/XfpapBbcOoy4.png?imageslim)

   ![mark](http://qnpic.sijihaiyang.top/blog/20190218/EplIayzlF2as.png?imageslim)

   ![mark](http://qnpic.sijihaiyang.top/blog/20190218/dgfzd9NWwQjQ.png?imageslim)

   ![mark](http://qnpic.sijihaiyang.top/blog/20190218/XKCwszdB1fSo.png?imageslim)

   

