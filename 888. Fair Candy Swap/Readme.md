888.py 用暴力求解的方式，嵌套遍历两个数组，逐个进行交换。复杂度为 $O(m\times n)$。最终 Time Exceeded。

better.py
利用公式
交换 x, y 后两边加和相等
$S_A​−x+y=S_B​−y+x$
$y = x + \frac{S_B - S_A}{2}$

268 题同样也是巧妙的公式运用