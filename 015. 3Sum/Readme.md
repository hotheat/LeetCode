`15.py` 利用第 0 题 Two sum 的思路，如果 a+b+c = 0，那么 a+b = -c，嵌套两层遍历列表，判断 -(a+b) 是否在列表中， 但是这样没法解决重复结果的问题。比如在结果中出现 [-1, 1, 0] 和 [0, 1, -1]。

先排序，排序的目的，三个数之和是由 min, mid 和 max 构成的，方便通过遍历来查找。

遍历元素 i 时，设置两个指针，前指针每次为 i+1，后指针为 n-1，前指针每次加 1，后指针每次减 1。 利用与上一个元素是否相同来去重复。直到前指针等于后指针时，i 再向前加 1。
nums = [-4, -1, -1, 0, 1, 2]
如果遍历到 i==2 时，判断 nums[2] 是否等于 nums[1]，如果相等，那么直接跳过。

`other.py` 把重复判断放在 if 条件里面，没有在外面进行判断。

[https://www.youtube.com/watch?v=gq-uWp327m8](https://www.youtube.com/watch?v=gq-uWp327m8)