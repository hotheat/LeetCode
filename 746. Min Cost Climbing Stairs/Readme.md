爬楼梯问题，当前位置的值是过路费（cost），每次可以爬一个格子或两个格子，可以从第一个格子或第二个格子开始爬。
要求爬完的代价最小，这是典型的动态规划问题。



一种解题思路：

当前的最小代价 dp(i) 等于 i-1 位置的最小代价加上 cost[i-1] 和 i-2 位置的最小代价加上 cost[i-2] 中的最小值，位置 i 处的代价不用进行计算。

dp(i) 代表爬到第 i 阶处的最小代价，**有两种可能性，要么从 i-1 阶爬上来，要么从 i-2 阶爬上来**。

`dp(i) = min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])`

最终答案是 `dp(len(cost))`

1. 记忆化递归 `746.py`

   将每一步的最小代价用字典存起来，用递归的方式求解。

2. 动态规划 `dp.py`

   计算每一阶楼梯的最小代价。

上述两种方法的时间复杂度和空间复杂度均是 O(n)，其实只需要记录 i-1 和 i-2 步的代价，然后进行更新即可，这样空间复杂度降为 O(1)。

3. 优化后的动态规划 `dp_opt.py`

   只更新 dp_i1 和 dp_i2 两个位置的值即可

   ![mark](http://qnpic.sijihaiyang.top/blog/180925/gcIam07dH3.png)