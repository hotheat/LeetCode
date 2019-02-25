这里的二叉查找树要求更严格一些

- 当前节点大于所有左子节点的最大值
- 当前节点小于所有右子节点的最小值

如果按照题意直接来求最大值和最小值，代码不好写，而且思路太绕。

这样考虑，每个节点都有一个范围，

![mark](http://qnpic.sijihaiyang.top/blog/20190225/z3a2voUHKkwS.png?imageslim)

每次只要判断节点是否在这个范围内就可以，而不需要管最大值和最小值如何变化的。

`098.py`，用 BFS 的方法，同样采用 BFS 还有 104 题，求二叉树的最大深度。

`recur.py`，用递归的方法

[https://www.youtube.com/watch?reload=9&v=DYNiCaKHneY](https://www.youtube.com/watch?reload=9&v=DYNiCaKHneY)