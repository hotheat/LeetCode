本题和 15 题类似，思路同样是遍历列表元素 i，同时设置两个指针 pre 和 beh，记录 i，pre 和 beh 三个位置的加和 s，如果 abs(s-target) 的值小于 abs(result-target)，令 target=s，获得与 target 差值最小的 result。

注意：result 的初始化为前三个元素的加和，可以防止列表元素小于 3 个的情况。

![mark](http://qnpic.sijihaiyang.top/blog/20190202/gTCy3r16oQWJ.png?imageslim)