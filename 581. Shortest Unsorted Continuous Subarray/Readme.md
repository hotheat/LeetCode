这道题没做出来，原因没想到用排序的方式，只想着从头遍历，暴力求解了。

other.py 中
利用排序，时间复杂度 $O(nlog_n)$，空间复杂度 $O(n)$

581.py 中
![mark](http://owzhgmyq5.bkt.clouddn.com/blog/180918/EeB9ja5lj9.png)
找到第一个开始下降的元素（从后往前找），
找到最后一个一直上升的元素（从前往后找），
和自己开始时想的一样，
参考 Discuss 中 Java 的答案。
时间复杂度 $O(n)$，空间复杂度 $O(1)$


